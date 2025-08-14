import json
import time
from flask import Response, render_template, request, session, stream_with_context
from app import app
from app.helpers import BasicResponse, generate_string


@app.route('/', methods=['GET'])
def index():
    ''' Display the Home page with default session values '''
    has_numbers = session.get('has_numbers', 0)
    has_lowercases = session.get('has_lowercases', 0)
    has_uppercases = session.get('has_uppercases', 0)
    has_blanks = session.get('has_blanks', 0)

    return render_template(
        'index.html', has_numbers=has_numbers,
        has_lowercases=has_lowercases,
        has_uppercases=has_uppercases,
        has_blanks=has_blanks
    )


@app.route('/sessions', methods=['POST'])
def setup_session():
    ''' Set the session, which would be used for the generation of strings '''
    try:
        session['has_numbers'] = int(request.form.get('hasNumbers', 0))
        session['has_lowercases'] = int(request.form.get('hasLowercases', 0))
        session['has_uppercases'] = int(request.form.get('hasUppercases', 0))
        session['has_blanks'] = int(request.form.get('hasBlanks', 0))

        res200: BasicResponse = {'error': 0, 'message': 'OK'}
        return Response(response=json.dumps(res200), status=200)
    except Exception as e:
        res400: BasicResponse = {'error': 1, 'message': str(e)}
        return Response(response=json.dumps(res400), status=400)


@app.route('/generate', methods=['GET'])
def generate_string_v1():
    ''' The trackable API with progress updates '''

    # Get the request's arguments, which are the input's values
    amount = int(request.args.get('amount', 1))
    length = int(request.args.get('length', 1))

    def process():
        ''' Processing the provided data and yielding events that are capturable in client-side '''
        for index in range(amount):
            # The process for tracking, which is generating a randomized string of a certain length
            generated_string = generate_string(
                length, has_number=session['has_numbers'],
                has_lowercase=session['has_lowercases'],
                has_uppercase=session['has_uppercases'],
                has_blanks=session['has_blanks']
            )
            # Simulate a progressing time, since generating a string is quite quick
            time.sleep(1.5)

            # Create a progress update message
            progress_data = {
                'item_number': index + 1,
                'total_items': amount,
                'current_item': index,
                'processed_value': generated_string,
                'progress': int(((index + 1) / amount) * 100)
            }

            # The SSE format: data: [JSON string]\n\n
            yield f"data: {json.dumps(progress_data)}\n\n"

        # When the loop is done, send a "complete" event
        yield "event: complete\n"
        yield "data: Job finished successfully!\n\n"

    return (Response(stream_with_context(process()), mimetype="text/event-stream"))
