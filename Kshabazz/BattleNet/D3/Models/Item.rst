-------------------------------------
Kshabazz\\BattleNet\\D3\\Models\\Item
-------------------------------------

.. php:namespace: Kshabazz\\BattleNet\\D3\\Models

.. php:class:: Item

    Class Item
    http://us.battle.net/api/d3/data/item/Cj0I-bvTgAsSBwgEFdosyssdb2mxyh10HmzAHfKS3AgdcIt38CILCAEVbEIDABgWICAwiQI4_AJAAFAMYJUDGMvMrsMGUABYAg&extra=0&showClose=1

    .. php:attr:: offHandTypes

    .. php:attr:: oneHandWeaponTypes

    .. php:attr:: twoHandedWeaponTypes

    .. php:method:: __construct($pJson)

        Constructor

        :type $pJson: string
        :param $pJson:

    .. php:method:: __get($pName)

        Get any property that isset.

        :param $pName:
        :returns: mixed

    .. php:method:: __toString()

        What to do when this object is converting to a string.

        :returns: string

    .. php:method:: damage()

        Compute [min, max] damage for the tool-tip.

        Damage the item can do, if weapon.

        :returns: mixed

    .. php:method:: effects()

        Get name of an items special effects.
        Get list string of item effect.

        :returns: string

    .. php:method:: id()

        Get item ID.

        :returns: mixed

    .. php:method:: init()

        Initialize all the properties for this object.

    .. php:method:: isWeapon()

        Check if an items type is a weapon.

        :returns: bool

    .. php:method:: json()

        Get JSON use to initialize this object.

        :returns: string

    .. php:method:: name()

        Get name.

        :returns: string

    .. php:method:: recipe()

        Get recipe for constructing the item at the forge.

        :returns: object

    .. php:method:: tooltipParams()

        Get web HASH.

        :returns: string

    .. php:method:: type()

        Get the item type.

        :returns: string
