## time-tracker-webservice  solution
import flask
import pprint

app = flask.Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': u'fixing bug #1',
        'time_spent': 20  # in mins
    },
    {
        'id': 2,
        'name': u'customer support',
        'time_spent': 30
    }
]

# find the task from the list, None if not found
def find_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task


@app.route('/')
def index():
    ret_value = {'status' : 'ok'}
    return flask.jsonify(ret_value)

## ----------- list all tasks --------
@app.route('/tasks/', methods=['GET'])
@app.route('/tasks/list', methods=['GET'])
def get_tasks_list():
    ## TODO
    ## Hint : set tasks as 'tasks'
    ret_value = {'status' : 'ok',\
                 'tasks' : '???'}
    if app.debug:
        print("get_tasks_list:Returning \n{}".format(pprint.pformat(ret_value, indent=4)))
    return flask.jsonify(ret_value)
## ----------- end: list all tasks --------


## ----------- get ONE task --------
@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    ret_value = {}
    task = find_task(task_id)
    if task:
        ## TODO : set task to the found task
        ## Hint :
        ret_value['status'] = 'ok'
        ret_value['task'] = '???'
    else:
        ret_value['status'] = 'error'
        ret_value['description'] = 'no task with id {}'.format(task_id)
        #flask.abort(404)

    if app.debug:
        print("get_task:Returning \n{}".format(pprint.pformat(ret_value, indent=4)))
    return flask.jsonify(ret_value)
## ----------- end: get ONE task --------

## ----------- create new task --------
@app.route('/task/new', methods=['POST'])
def create_task():
    ret_value = {}
    if not flask.request.json or not 'name' in flask.request.json:
        ret_value['status'] = 'error'
        ret_value['description'] = "need 'name' for task"
    else: # create a new task
        ## TODO : create a task
        ## Hint : name = flask.request.json['name']
        ## Hint : time_spent = 0
        task =  {
            'id': tasks[-1]['id'] + 1,
            'name': '???',
            'time_spent' : '???'
        }

        ## TODO : append the newly created task to the tasks list
        ## Hint : append
        # tasks.???(task)

        ret_value['status'] = 'ok'
        ret_value['task'] = task

    if app.debug:
        print("get_task:Returning \n{}".format(pprint.pformat(ret_value, indent=4)))
    return flask.jsonify(ret_value)
## ----------- end: create new task --------


## ----------- update a task --------
@app.route('/task/update/<int:task_id>', methods=['PUT', 'POST'])
def update_task(task_id):
    ret_value = {}
    task = find_task(task_id)
    if not task:
        ret_value['status'] = 'error'
        ret_value['description'] = 'no task with id {}'.format(task_id)
        if app.debug:
            print("get_task:Returning \n{}".format(pprint.pformat(ret_value, indent=4)))
        return flask.jsonify(ret_value)
        #flask.abort(404)
    if not flask.request.json:
        ret_value['status'] = 'error'
        ret_value['description'] = 'missing parameters'
        if app.debug:
            print("get_task:Returning \n{}".format(pprint.pformat(ret_value, indent=4)))
        return flask.jsonify(ret_value)

    if not 'time' in flask.request.json:
        ret_value['status'] = 'error'
        ret_value['description'] = "missing 'time'"
        if app.debug:
            print("get_task:Returning \n{}".format(pprint.pformat(ret_value, indent=4)))
        return flask.jsonify(ret_value)

    # now update the task
    time = flask.request.json['time']
    ## TODO : add time to time_spent below
    # task ['time_spent'] += int(???)

    ret_value['status'] = 'ok'
    ret_value['task'] = task
    if app.debug:
        print("get_task:Returning \n{}".format(pprint.pformat(ret_value, indent=4)))
    return flask.jsonify(ret_value)
## ----------- end : update a task --------

## ----------- delete a task --------
@app.route('/task/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = find_task(task_id)
    if not task:
        ret_value = { 'status' : 'error',
                      'description' : 'no task with id {}'.format(task_id)}
        if app.debug:
           print("get_task:Returning \n{}".format(pprint.pformat(ret_value, indent=4)))
        return flask.jsonify(ret_value)
        #flask.abort(404)

    ## TODO : remove the task from tasks list below
    ## hint : remove
    # tasks.???(task)
    ret_value = { 'status' : 'ok',
                  'description' : 'removed task id {}'.format(task_id)}
    if app.debug:
        print("get_task:Returning \n{}".format(pprint.pformat(ret_value, indent=4)))
    return flask.jsonify(ret_value)
## ----------- end : delete a task --------

if __name__ == '__main__':
    app.run(debug=True)
