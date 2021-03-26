# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NewRaptor
                                 A QGIS plugin
 Add a new raptor nest,create buffer and impact table
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-03-23
        copyright            : (C) 2021 by shubham
        email                : Shubham
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load NewRaptor class from file NewRaptor.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .new_raptor import NewRaptor
    return NewRaptor(iface)
