from openai import OpenAI

ERR_MSG = "ERRORERRORERRORERROR"
DONE_MSG = "LABELIZATIONCOMPLETE"


def send_message(client, thread, assistant, payload):
    _ = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=payload
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    # print(run.status)

    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    response = None
    for content in messages.data[0].content:
        if content.type == 'text':
            response = content.text.value

    return response


def labelize_transcript(api_key, transcript):
    client = OpenAI(
        api_key=api_key,
    )

    assistant = client.beta.assistants.create(
        instructions=f"You will be provided a user interview transcript. \
            Assign speaker labels to the transcript \
            (#### Interviewer, #### Interviewee). \
            Insert a new line between speaker blocks. \
            Return just the labeled transcript, \
            without any additional text before or after. \
            Please fix any semantic and logical errors \
            you find within the script since it's extracted using Whisper. \
            Append {DONE_MSG} at the end, alone on a new line. \
            If any of this is not possible or you encounter an error, \
            just write {ERR_MSG}",
        # model="gpt-4-turbo-preview",
        model="gpt-3.5-turbo-0125",
    )

    thread = client.beta.threads.create()

    response = send_message(client, thread, assistant, transcript)
    labelized = response

    while labelized[-20:] not in [ERR_MSG, DONE_MSG]:
        # print(labelized[-20:])
        if labelized[-20:] == ERR_MSG:
            return ERR_MSG

        response = send_message(client, thread, assistant, "Continue")
        labelized += response

    return labelized[:-20]


def summarize(api_key, idea_summary, transcript):
    client = OpenAI(
        api_key=api_key,
    )

    instructions = f"""You are an experienced user researcher.
You will receive a user research interview transcript.
Please summarize it, and extract key themes and key quotes \
that would be most useful to development of the following idea.
Be verbose in your answer.

{idea_summary}"""

    assistant = client.beta.assistants.create(
        instructions=instructions,
        model="gpt-4-0125-preview",
    )

    thread = client.beta.threads.create()

    response = send_message(client, thread, assistant, transcript)

    return response
