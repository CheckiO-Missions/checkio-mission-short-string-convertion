"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ['line1', 'line1'],
            "answer": 0
        },
        {
            "input": ['line1', 'line2'],
            "answer": 1
        },
        {
            "input": ['line', 'line2'],
            "answer": 1
        },
        {
            "input": ['ine', 'line2'],
            "answer": 2
        },
        {
            "input": ['line1', '1enil'],
            "answer": 4
        },

        {
            "input": ['', ''],
            "answer": 0
        },
        {
            "input": ['l', ''],
            "answer": 1
        }

    ]
}
