#!/usr/bin/env python3

# A graphial interface to select page formats.


import json
import PySimpleGUI as sg


def load_paper_data(standards = '', formats = '', units = ''):

    # Load paper data from reference file into a dictionary.
    with open('all_paper_sizes.json') as file_paper_sizes:
        data_paper_sizes = json.load(file_paper_sizes)

    # Report to console recieved parameters
    if standards != '':
        print('\n-------------\n  SELECTION \n-------------')
        print('load_paper_data():')
        print('> standards = {}'.format(standards))
        print('> formats = {}'.format(formats))
        print('> units = {}'.format(units))
        # print('> sizes = {}'.format(paper_data['paper_sizes']))
        print('-------------')

    # Dictionary for returning values of paper selections
    paper_data = {
        "paper_standards": [],
        "paper_formats": [],
        "paper_units": [],
        "paper_sizes": [],
    }

    # Populate "paper_standards".
    # Return dictionary with "paper_standards"
    if standards == '':
        for standard, void in data_paper_sizes.items():
            paper_data["paper_standards"].append(standard)
        print('\n-------------')
        print('> standards = {}'.format(paper_data['paper_standards']))
        print('-------------')
        return paper_data

    # Select a paper standard if argument provided
    # then populate "paper_formats".
    if standards != '':
        for formats, void in data_paper_sizes[standards].items():
            paper_data['paper_formats'].append(formats)
        print('\n-------------')
        print('> formats = {}'.format(paper_data['paper_formats']))
        print('-------------')
        # return paper_data

    if formats != '':
        for units, void in data_paper_sizes[standards][formats].items():
            paper_data['paper_units'].append(units)
        # for sizes, void in data_paper_sizes[standards][formats][units]:
        paper_data['paper_sizes'] = data_paper_sizes[standards][formats][units]

        print('\n-------------')
        print('> units = {}'.format(paper_data['paper_units']))
        print('> sizes = {}'.format(paper_data['paper_sizes']))
        print('-------------')
        # return paper_data

    if units != '':
        # paper_data['paper_sizes'] = data_paper_sizes[standards][formats][units].items()
        paper_data['paper_sizes'] = data_paper_sizes[standards][formats][units]
        print('\n-------------')
        print('> sizes = {}'.format(paper_data['paper_sizes']))
        # print('> dimension = {}'.format(paper_data['paper_sizes']))
        print('-------------')

    return paper_data


def draw_window(paper_data = None):

    options = {
        "font": ('Helvetica', 16),
        "size": (40, 1),
        "readonly": True,
        "enable_events": True,
    }

    layout = [
       [sg.Combo(list(paper_data["paper_standards"]), **options, key="paper_standards")],
       [sg.Combo((), **options, key="paper_formats")],
       [sg.Combo((), **options, key="paper_units")],
       [sg.Text('DIMENSTION', key='-DIMENSION-')],
       # [sg.Combo((), **options, key="paper_sizes")],
       # [sg.InputText(default_text = 'Default text', key='_DIMENSION_BOX_')],
       # [sg.Text()],
    ]

    return sg.Window('Page Size Selector', layout, keep_on_top=True)


def  evaluate_window(window = None):
    while True:

        event, values = window.read()
        print('\n-------------')
        print('> event = {}'.format(event))
        print('> values[paper_standards] = {}'.format(values['paper_standards']))
        print('> values[paper_formats] = {}'.format(values['paper_formats']))
        print('> values[paper_units] = {}'.format(values['paper_units']))
        # print('> values[{}] = {}'.format(event, values[event]))
        print('-------------')

        if event == sg.WINDOW_CLOSED:
            break

        elif event == 'paper_standards':
            seletion_paper_standard = values[event]
            paper_data = load_paper_data(standards = seletion_paper_standard, formats = None, units = None)
            window['paper_formats'].Update(value = paper_data['paper_formats'][0], values = paper_data['paper_formats'])

        elif event == 'paper_formats':
            seletion_paper_format = values[event]
            paper_data = load_paper_data(standards = seletion_paper_standard, formats = seletion_paper_format, units = None)
            window['paper_units'].Update(value = paper_data['paper_units'][0], values = paper_data['paper_units'])
            # window['paper_units'].Update(value = 'test', values = 'tests')

        elif event == 'paper_units':
            seletion_paper_unit = values[event]
            print('\n-------------')
            print('paper_units: {}'.format(values[event]))
            print('-------------')
            paper_data = load_paper_data(standards = seletion_paper_standard, formats = seletion_paper_format, units = seletion_paper_unit)
            paper_size = str(paper_data['paper_sizes'][0]) + ' x ' + str(paper_data['paper_sizes'][1])
            print('\n-------------')
            print('paper_size: {}'.format(paper_size))
            print('-------------')            # window['paper_sizes'].Update(value = paper_size, values = paper_data['paper_sizes'])
            window['-DIMENSION-'].update(paper_size)
            # window.Element('_DIMENSION_BOX_').update(default_text = values)
        # elif event == "paper_sizes":
        #     lst = paper_data[values[event]]
        #     window['paper_sizes'].Update(value=lst[0], values=lst)

    window.close()

def main():

    # Create paper_data object for summoning paper sizes.
    paper_data = load_paper_data()

    # Create a window object for evaluating with given paper data.
    PaperSizeSelector_window = draw_window(paper_data)

    # Evaluate the window actions.
    evaluate_window(PaperSizeSelector_window)

# Starting from terminal
if __name__ == "__main__":

    # Go into the program function
    main()

