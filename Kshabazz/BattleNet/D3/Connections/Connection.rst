------------------------------------------------
Kshabazz\\BattleNet\\D3\\Connections\\Connection
------------------------------------------------

.. php:namespace: Kshabazz\\BattleNet\\D3\\Connections

.. php:class:: Connection

    Interface Resource

    .. php:method:: getHero($pHeroId)

        Request Hero JSON from Battle.Net.
        ex:
        http://us.battle.net/api/d3/profile/<battleNetIdName>-<battleNetIdNumber>/hero/<hero-id>
        Note: Leave off the trailing '/' when setting

        :param $pHeroId:
        :returns: string|null

    .. php:method:: getItem($pItemId)

        Get item JSON from Battle.Net D3 API.
        ex:
        http://us.battle.net/api/d3/data/item/COGHsoAIEgcIBBXIGEoRHYQRdRUdnWyzFB2qXu51MA04kwNAAFAKYJMD

        :param $pItemId:
        :returns: string|null

    .. php:method:: getItemsAsModels($pItemHashes)

        For each item the hero in the array construct an Model\Item and return
        them as an array.

        :type $pItemHashes: array
        :param $pItemHashes: List of item hashes.
        :returns: array|null

    .. php:method:: getProfile()

        ex:
        http://us.battle.net/api/d3/profile/<battleNetIdName>-<battleNetIdNumber>/

        :returns: string|null
