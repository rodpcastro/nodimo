from sympy import Symbol


class Variable(Symbol):
    """Creates a symbolic variable.

    This is the most basic element that is used to build all the other
    classes in this project. It inherits from the sympy Symbol class the
    ability to be used in mathematical expressions, and adds to it a few
    attributes that are useful in describing its dimensional properties.

    Attributes
    ----------
    name: str
        The name that will be displayed in symbolic expressions.
    dimensions: dict[str, int]
        Dictionary containing dimensions' names and exponents.
    is_dependent: bool
        If True, the variable is dependent.
    is_scaling: bool
        If True, the variable can be used as scaling parameter.
    is_nondimensional: bool
        If True, the variable is nondimensional.

    Alias
    -----
    Var

    Examples
    --------
    >>> from nodimo import Variable
    Considering the dimensions mass (M), length (L) and time (T), a
    force F can be defined as:
    >>> F = Variable('F', M=1, L=1, T=-2)
    To define a nondimensional variable A is sufficient to provide
    just its name:
    >>> A = Variable('A')
    To use a greek letter in symbolic expressions, just provide its
    english representation as the name of the variable:
    >>> a = Variable('alpha')
    """

    def __new__(cls,
                name: str,
                dependent: bool = False,
                scaling: bool = False,
                **dimensions: int):
        
        return super().__new__(cls, name)

    def __init__(self,
                 name: str,
                 dependent: bool = False,
                 scaling: bool = False,
                 **dimensions: int):
        """
        Parameters  
        ----------
        name: str
            The name that will be displayed in symbolic expressions.
        dependent: bool, optional (default=False)
            If True, the variable is dependent.
        scaling: bool, optional (default=False)
            If True, the variable can be used as scaling parameter.
        **dimensions: int
            The dimensions of the variable given as keyword arguments.

        Raises
        ------
        ValueError
            If the variable is set as both dependent and scaling.
        ValueError
            If the variable is set as scaling, but with no dimensions.
        """

        super().__init__()
        self.dimensions: dict[str, int] = dimensions
        self.is_dependent: bool = dependent
        self.is_scaling: bool = scaling
        self.is_nondimensional: bool = all(dim == 0
                                           for dim in self.dimensions.values())

        if self.is_dependent and self.is_scaling:
            raise ValueError(
                "A variable can not be both dependent and scaling")

        if self.is_scaling and self.is_nondimensional:
            raise ValueError(
                "A variable can not be both scaling and nondimensional")


# Alias for the class Variable.
Var = Variable
