

### 1 dict
recorder = {
    'plot': {},
    'line': {},
    'scatter': {},
    'image': {},
    'text': {},
    'fixations': {},
}

def record(name, value, data_type='plot'):
    if data_type in ['plot', 'scatter']:
        try:
            # try expend
            ## if recorder[data_type][name] has value, then can append data, else exception
            recorder[data_type][name] += [value]
            print('>>>1')
        except Exception as e:
            # else, initialize
            recorder[data_type][name] = [value]
            print('>>>2')
    else:
        recorder[data_type][name] = value

eg1:
record('crossentropy', [0, 1], data_type='plot')
>>>
>>>2
{'image': {}, 'fixations': {}, 'plot': {'crossentropy': [[0, 1]]}, 'scatter': {}, 'line': {}, 'text': {}}

eg2:
record('crossentropy', [0, 1], data_type='plot')
record('crossentropy', [0, 2], data_type='plot')
>>>
>>>2
>>>1
{'fixations': {}, 'line': {}, 'scatter': {}, 'image': {}, 'text': {}, 'plot': {'crossentropy': [[0, 1], [0, 2]]}}

eg3:
record('crossentropy', [0, 1], data_type='image')
>>>
{'line': {}, 'plot': {}, 'text': {}, 'fixations': {}, 'image': {'crossentropy': [0, 1]}, 'scatter': {}}

eg4:
>>>
record('crossentropy', [0, 1], data_type='image')
record('crossentropy', [0, 2], data_type='image')

{'plot': {}, 'text': {}, 'fixations': {}, 'scatter': {}, 'line': {}, 'image': {'crossentropy': [0, 2]}}
