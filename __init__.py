# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HAProjectSetup
                                 A QGIS plugin
 This plugin is for project setup and setup QC.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-02-06
        copyright            : (C) 2025 by Lei Ding
        email                : lei.ding@headlandarchaeology.com
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
    """Load HAProjectSetup class from file HAProjectSetup.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ha_project_setup import HAProjectSetup
    return HAProjectSetup(iface)
