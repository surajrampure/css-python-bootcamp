test = {   'name': 'q1g',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> t1 = optimal_route({'SAN', 'DEN', 'BOS'})\n>>> t1 == ('BOS', 'DEN', 'SAN') or t1[::-1] == ('BOS', 'DEN', 'SAN')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> t2 = optimal_route({'SAN', 'BOM', 'LHR', 'CDG', 'SLC', 'MSP'})\n"
                                               ">>> t2 == ('SAN', 'SLC', 'MSP', 'LHR', 'CDG', 'BOM') or t2[::-1] == ('SAN', 'SLC', 'MSP', 'LHR', 'CDG', 'BOM')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> t3 = optimal_route({'SIN', 'DTW', 'LAX', 'EWR', 'DPS'})\n"
                                               ">>> t3 == ('SIN', 'DPS', 'LAX', 'DTW', 'EWR') or t3[::-1] == ('SIN', 'DPS', 'LAX', 'DTW', 'EWR')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
