"""This module contains variables and functions for internal use.

Variables
---------
_is_running_on_jupyter : bool
    If ``True``, the package in running on jupyter notebooks.

Functions
---------
_show_object(obj)
    Prints object in shell.
_print_horizontal_line()
    Prints a horizontal line.
_print_warning(message)
    Prints a message with warning colors.
_remove_duplicates(original_list)
    Removes duplicates from a list, keeping the order.
_obtain_dimensions(*variables)
    Obtains the dimensions' names from the given variables.
_build_dimensional_matrix(variables, dimensions=[])
    Builds a basic dimensional matrix.
"""

import sympy as sp
import warnings

try:
    from IPython import get_ipython

    _is_running_on_jupyter = True if get_ipython() is not None else False
    if not _is_running_on_jupyter:
        raise
    from IPython.display import display, Markdown, HTML
except:
    _is_running_on_jupyter = False


def _custom_display(obj):
    """Displays object using a custom CSS style.

    This custom display function was created to avoid vertical scrolling
    bars on the right of cells outputs, specially when running jupyter
    notebook in Google Chrome (issue #10 on github repository).

    Parameters
    ----------
    obj : Any
        The object to print.
    """

    css_style = ('<style>.jp-OutputArea-output{'
        'overflow-y: hidden;'
    '}</style>')

    display(HTML(css_style + f'${obj._repr_latex_()}$'))


def _show_object(obj, use_custom_css=True):
    """Prints object in shell.

    Parameters
    ----------
    obj : Any
        The object to print.
    use_custom_css : bool, default=True
        If ``True``, the object is displayed using custom css.
    """

    if _is_running_on_jupyter:
        if use_custom_css:
            _custom_display(obj)
        else:
            display(obj)
    else:
        print('\n' + sp.pretty(obj, root_notation=False) + '\n')


def _print_horizontal_line():
    """Prints a horizontal line."""

    if _is_running_on_jupyter:
        display(Markdown('<hr>'))
    else:
        print(78 * '-')


def _remove_duplicates(original_list):
    """Removes duplicates from a list, keeping the order.

    Parameters
    ----------
    original_list : list
        List to be checked for duplicates.

    Returns
    -------
    new_list : list
        List with duplicates removed.
    """

    new_list = []
    for e in original_list:
        if e not in new_list:
            new_list.append(e)

    return new_list


def _obtain_dimensions(*variables):
    """Obtains the dimensions' names from the given variables.

    Parameters
    ----------
    *variables : Variable
        Variables to get the dimensions extracted.

    Returns
    -------
    dimensions : list[str]
        List containing the dimensions' names.
    """

    dimensions = []

    for var in variables:
        dimensions += list(var.dimensions.keys())

    dimensions = _remove_duplicates(dimensions)

    return dimensions


def _build_dimensional_matrix(variables, dimensions=[], return_raw=False):
    """Builds a basic dimensional matrix.

    A basic dimensional matrix contains only numbers, no labels.

    Parameters
    ----------
    variables : list[Variable]
        List with the variables used to build the dimensional matrix.
    dimensions : list[str], default=[]
        List with the dimensions' names of the given variables. If not
        provided, this list is obtained from the variables.
    return_raw : bool, defaul=True
        If ``True``, return matrix will be a list of lists.

    Returns
    -------
    dimensional_matrix : Matrix or list[list[int]]
        Matrix with one column for each variable, one row for each
        dimension, and every entry represents the dimension's exponent
        of a particular variable.
    """

    if len(variables) > 0 and dimensions == []:
        dimensions = _obtain_dimensions(*variables)

    raw_dimensional_matrix = []

    for dim in dimensions:
        dimension_exponents = []

        for var in variables:
            if dim in var.dimensions.keys():
                dimension_exponents.append(var.dimensions[dim])
            else:
                dimension_exponents.append(0)

        raw_dimensional_matrix.append(dimension_exponents)

    dimensional_matrix = sp.Matrix(raw_dimensional_matrix)
    dimensional_matrix = sp.nsimplify(dimensional_matrix,
                                      rational=True).as_mutable()

    if return_raw:
        return raw_dimensional_matrix
    else:
        return dimensional_matrix


class UnrelatedVariableWarning(Warning):
    """Unrelated variable warning.
    
    Issued when a variable can not be used and, therefore, is discarded.
    """

    pass


warnings.simplefilter('always', UnrelatedVariableWarning)


def custom_formatwarning(message, category, filename, lineno, line=None):
    """Custom format for warning messages."""

    return f'{category.__name__}: \033[93m{message}\033[0m\n'


warnings.formatwarning = custom_formatwarning


def _show_warning(message: str, category: Warning):
    """Displays a message with warning colors."""

    warnings.warn(message, category)
