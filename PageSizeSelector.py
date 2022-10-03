#!/usr/bin/env python3

# A graphial interface to select page formats.


import json
import PySimpleGUI as sg
from os import system


def clear():
    """This function only has support to clear the screen for Linux of Mac."""
    _ = system("clear")


# def load_paper_data(standards = '', formats = '', unit = ''):
def load_paper_data(standards = '', formats = '', units = '', unit = ''):

    # Load paper data from reference file into a dictionary.
    with open('all_paper_sizes.json') as file_paper_sizes:
        data_paper_sizes = json.load(file_paper_sizes)

    # Dictionary for returning values of paper selections
    paper_data = {
        "paper_standards": [],
        "paper_formats": [],
        "paper_units": [],
        "paper_sizes": [],
    }

    # # Report to console recieved parameters
    # if standards != '':
    #     print('\n-------------\n  SELECTION \n-------------')
    #     print('load_paper_data():')
    #     print('> standards = {}'.format(standards))
    #     print('> formats = {}'.format(formats))
    #     print('> units = {}'.format(units))
    #     # print('> sizes = {}'.format(paper_data['paper_sizes']))
    #     print('-------------')

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
        print('> standards = {}'.format(standards))
        print('> formats = {}'.format(paper_data['paper_formats']))
        print('-------------')
        # return paper_data

    if formats != '':
        print('data_paper_sizes[standards][formats].items(): {}'.format(type(data_paper_sizes[standards][formats].items())))
        print('data_paper_sizes[standards][formats].items(): {}'.format(data_paper_sizes[standards][formats].items()))
        print('paper_data[\'paper_units\']: {}'.format(type(paper_data['paper_units'])))
        print('paper_data[\'paper_units\']: {}'.format(paper_data['paper_units']))

        for units, void in data_paper_sizes[standards][formats].items():
            print(units)
            paper_data['paper_units'].append(units)
        # paper_data['paper_units'] = units
        # for sizes, void in data_paper_sizes[standards][formats][units]:
            # print(sizes)
            # paper_data['paper_sizes'].append(sizes)

        # for sizes, void in data_paper_sizes[standards][formats][units]:
        # paper_data['paper_sizes'] = data_paper_sizes[standards][formats][0]
        paper_data['paper_sizes'] = data_paper_sizes[standards][formats][units]
        # paper_data['paper_sizes'] = data_paper_sizes[standards][formats][unit]
        print('type(data_paper_sizes): {}'.format(type(data_paper_sizes)))
        print('type(data_paper_sizes[standards][formats]): {}'.format(type(data_paper_sizes[standards][formats])))
        print('data_paper_sizes[standards][formats]: {}'.format(data_paper_sizes[standards][formats]))
        print('type(data_paper_sizes[standards][formats][units]): {}'.format(type(data_paper_sizes[standards][formats][units])))
        print('data_paper_sizes[standards][formats][units]: {}'.format(data_paper_sizes[standards][formats][units]))
        print('data_paper_sizes[standards][formats][units][0]: {}'.format(data_paper_sizes[standards][formats][units][0]))
        print('-------------')


        # if units == 'mm':
        #     units = 0
        # elif units == 'points':
        #     units = 1
        # elif units == 'inches':
        #     units = 2

        print('\n-------------')
        print('> standards = {}'.format(standards))
        print('> formats = {}'.format(formats))
        print('> units = {}'.format(units))
        print('> paper_data[\'paper_units\'] = {}'.format(paper_data['paper_units']))
        print('> unit = {}'.format(unit))
        print('-------------')
        if unit != '':
            print(data_paper_sizes[standards][formats][unit])
            paper_data['paper_sizes'] = data_paper_sizes[standards][formats][unit]
        # for unit, value in data_paper_sizes[standards][formats].items():
            # print(unit + " => " + value)
        # print('> sizes = {}'.format(sizes))
        print('-------------')
        print('> units = {}'.format(paper_data['paper_units']))
        print('> sizes = {}'.format(paper_data['paper_sizes']))
        print('> sizes = {}'.format(paper_data['paper_sizes'][0]))
        # print('> sizes = {}'.format(paper_data['paper_sizes'][units))
        print('-------------')
        # return paper_data

    # if units != '':
    #     for sizes, void in data_paper_sizes[standards][formats].items():
    #         # print(sizes)
    #         paper_data['paper_units'].append(sizes)
    #     # paper_data['paper_sizes'] = data_paper_sizes[standards][formats][units].items()
    #     # paper_data['paper_sizes'] = data_paper_sizes[standards][formats][sizes]
    #     print('\n-------------')
    #     print('> sizes = {}'.format(paper_data['paper_sizes']))
    #     # print('> dimension = {}'.format(paper_data['paper_sizes']))
    #     print('-------------')

    return paper_data


def draw_window(paper_data = None):

    options = {
        "font": ('Helvetica', 16),
        "size": (40, 1),
        "readonly": True,
        "enable_events": True,
    }

    layout = [
       [sg.Text('paper_standards', key='-PAPER_STANDARDS-')],
       [sg.Combo(list(paper_data["paper_standards"]), **options, key="paper_standards")],
       [sg.Text('paper_formats', key='-PAPER_FORMATS-')],
       [sg.Combo((), **options, key="paper_formats")],
       [sg.Text('paper_units', key='-PAPER_UNITS-')],
       [sg.Combo((), **options, key="paper_units")],
       [sg.Text('paper_size', key='-PAPER_SIZE-')],
       [sg.Text('0 X 0', key='-PAPER_DIMENSION-'),
        sg.Text(paper_data['paper_units'])]
       # [sg.Combo((), **options, key="paper_sizes")],
       # [sg.InputText(default_text = 'Default text', key='_DIMENSION_BOX_')],
       # [sg.Text()],
    ]

    return sg.Window('Page Size Selector', layout, keep_on_top=True)


def  evaluate_window(window = None, paper_data = None):
    while True:

        event, values = window.read()
        # print('\n-------------')
        # print('> event = {}'.format(event))
        # print('> values[paper_standards] = {}'.format(values['paper_standards']))
        # print('> values[paper_formats] = {}'.format(values['paper_formats']))
        # print('> values[paper_units] = {}'.format(values['paper_units']))
        # # print('> values[{}] = {}'.format(event, values[event]))
        # print('-------------')

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
            # window['paper_units'].Update(value = paper_data['paper_units'][0], values = paper_data['paper_units'])
            # window['paper_units'].Update(value = 'test', values = 'tests')

        elif event == 'paper_units':
            seletion_paper_unit = values[event]
            paper_data = load_paper_data(standards = seletion_paper_standard, formats = seletion_paper_format, units = seletion_paper_unit, unit = seletion_paper_unit)
            paper_size = str(paper_data['paper_sizes'][0]) + ' x ' + str(paper_data['paper_sizes'][1])
            window['-PAPER_DIMENSION-'].update(paper_size)
            # print('\n-------------')
            # print('paper_units: {}'.format(values[event]))
            # print('-------------')
            # print('\n-------------')
            # print('paper_size: {}'.format(paper_size))
            # print('-------------')            # window['paper_sizes'].Update(value = paper_size, values = paper_data['paper_sizes'])
            # window.Element('_DIMENSION_BOX_').update(default_text = values)
        # elif event == "paper_sizes":
        #     lst = paper_data[values[event]]
        #     window['paper_sizes'].Update(value=lst[0], values=lst)

    window.close()

def main():

    # Empty the console screen.
    clear()

    # Create paper_data object for summoning paper sizes.
    paper_data = load_paper_data()

    # Create a window object for evaluating with given paper data.
    PaperSizeSelector_window = draw_window(paper_data)

    # Evaluate the window actions.
    evaluate_window(PaperSizeSelector_window, paper_data)

# Starting from terminal
if __name__ == "__main__":

    # Go into the program function
    main()

