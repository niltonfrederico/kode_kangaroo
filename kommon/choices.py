from copy import deepcopy


class Choices(object):
    """ 
    Extended from Django Model Utils, please refer to  
    https://django-model-utils.readthedocs.io/en/latest/utilities.html#choices 
    """

    def __init__(self, *choices):
        # list of choices expanded to triples - can include optgroups
        self._triples = []
        # list of choices as (db, human-readable) - can include optgroups
        self._doubles = []
        # dictionary mapping db representation to human-readable
        self._display_map = {}
        # dictionary mapping Python identifier to db representation
        self._identifier_map = {}
        # set of db representations
        self._db_values = set()

        self._process(choices)

    def _store(self, triple, triple_collector, double_collector):
        self._identifier_map[triple[1]] = triple[0]
        self._display_map[triple[0]] = triple[2]
        self._db_values.add(triple[0])
        triple_collector.append(triple)
        double_collector.append((triple[0], triple[2]))

    def _process(self, choices, triple_collector=None, double_collector=None):
        if triple_collector is None:
            triple_collector = self._triples
        if double_collector is None:
            double_collector = self._doubles

        store = lambda c: self._store(c, triple_collector, double_collector)

        for choice in choices:
            if isinstance(choice, (list, tuple)):
                if len(choice) == 3:
                    store(choice)
                elif len(choice) == 2:
                    if isinstance(choice[1], (list, tuple)):
                        # option group
                        group_name = choice[0]
                        subchoices = choice[1]
                        tc = []
                        triple_collector.append((group_name, tc))
                        dc = []
                        double_collector.append((group_name, dc))
                        self._process(subchoices, tc, dc)
                    else:
                        store((choice[0], choice[0], choice[1]))
                else:
                    raise ValueError(
                        "Choices can't take a list of length %s, only 2 or 3"
                        % len(choice)
                    )
            else:
                store((choice, choice, choice))

    def __len__(self):
        return len(self._doubles)

    def __iter__(self):
        return iter(self._doubles)

    def __reversed__(self):
        return reversed(self._doubles)

    def __getattr__(self, attname):
        try:
            return self._identifier_map[attname]
        except KeyError:
            raise AttributeError(attname)

    def __getitem__(self, key):
        return self._display_map[key]

    def __add__(self, other):
        if isinstance(other, self.__class__):
            other = other._triples
        else:
            other = list(other)
        return Choices(*(self._triples + other))

    def __radd__(self, other):
        # radd is never called for matching types, so we don't check here
        other = list(other)
        return Choices(*(other + self._triples))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._triples == other._triples
        return False

    def __repr__(self):
        return "%s(%s)" % (
            self.__class__.__name__,
            ", ".join(("%s" % repr(i) for i in self._triples)),
        )

    def __contains__(self, item):
        return item in self._db_values

    def __deepcopy__(self, memo):
        return self.__class__(*deepcopy(self._triples, memo))

