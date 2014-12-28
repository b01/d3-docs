--------------------------------
Kshabazz\\BattleNet\\D3\\Profile
--------------------------------

.. php:namespace: Kshabazz\\BattleNet\\D3

.. php:class:: Profile

    Class Profile

    .. php:method:: __construct($pJson)

        :param $pJson:

    .. php:method:: battleTag()

        Get battle net tag.

        :returns: string

    .. php:method:: get($pProperty)

        Get property

        :param $pProperty:

    .. php:method:: heroes()

        :returns: mixed Heroes(s) data as an array, or null if none.

    .. php:method:: getHero($pHeroByName)

        Get hero by name

        :type $pHeroByName: mixed
        :param $pHeroByName: string Optional name to specify a single hero to return.
        :returns: array|null

    .. php:method:: init()

        Initialize all the properties for this object.

        :returns: $this

    .. php:method:: json()

        Get raw JSON data returned from Battle.net.

    .. php:method:: jsonSerialize()

        Specify how this object is to be used with json_encode.

        :returns: \stdClass
