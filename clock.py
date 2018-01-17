#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################

from __future__ import division

import sys, sched, time
import threading as td
from datetime import datetime as dt
from PyQt5.QtCore import QPoint, Qt, QTime, QTimer, QThread
from PyQt5.QtGui import QColor, QPainter, QPolygon, QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                                QDialog, QDesktopWidget, QToolTip)

class AnalogClock(QWidget):
    hourHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -50)
    ])

    minuteHand = QPolygon([
        QPoint(7, 8),
        QPoint(-7, 8),
        QPoint(0, -75)
    ])

    secondHand = QPolygon([
        QPoint(2, 18),
        QPoint(-2, 18),
        QPoint(0, -90)
    ])

    hourColor = QColor(127, 0, 127, 191)
    minuteColor = QColor(0, 127, 127, 191)
    secondColor = QColor(127, 0, 0, 191)

    def __init__(self, parent=None):
        super(AnalogClock, self).__init__(parent)

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        self.setWindowIcon(QIcon('icon.ico'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self._tip = None
        self._top = "On Top"
        self._time = self.digitTime()
        self._tb = None
        self._alert = None

        self.resize(200, 200)
        
    
    def tooClose(self):
        w = 0.8
        s = QDesktopWidget().screenGeometry()
        r = (self.x() + self.width())/s.width()
        return r > w

    def showDialog(self):
        d = QDialog()

        d.setWindowFlag(Qt.FramelessWindowHint)
        d.setAttribute(Qt.WA_TranslucentBackground)
        d.setWindowIcon(QIcon('icon.ico'))

        names = ('Zoom In', 'Zoom Out', self._top, 
                 'Cancel', 'Exit', self._time)
        row = 0
        vw = 150
        vh = 40
        # opacity level
        max = 30
        min = 30
        lvl = min
        for name in names:
            b = QPushButton(name, d)
            b.move(0, row)
            b.resize(vw, vh-1)
            b.clicked.connect(self.do(name, d))
            ss = 'QPushButton { background-color: rgba(0, 0, 0, %d%%); color: #FFF; font-size: 12px; }'
            b.setStyleSheet( ss % lvl )
            if name == self._time:
                self._tb = b
                
            lvl += int((max-min) / (len(names)-1))
            row += vh

        if self.tooClose():
            d.move(self.x() - b.width(), self.y())
        else:
            d.move(self.x() + self.width(), self.y())

        d.setWindowTitle("Dialog")
        d.setWindowModality(Qt.ApplicationModal)
        ret = d.exec_()
        
    def do(self, v, d):
        def act():
            if v == self._top:
                if self._top == "On Top":
                    self._top = "Off Top"
                else:
                    self._top = "On Top"
                self.setWindowFlags(self.windowFlags() ^ Qt.WindowStaysOnTopHint)
                self.show()
                d.close()

            if v == "Zoom In":
                self.zoomin()
            if v == "Zoom Out":
                self.zommout()
            if v == "Exit":
                sys.exit()
            if v == "Cancel":
                d.close()

        return act

    def digitTime(self):
        text = time.strftime("%H"+":"+"%M"+":"+"%S")
        return text
    
    def paintEvent(self, event):
        
        global MSG
        
        if self._tip:
            QToolTip.showText(
                self.mapToGlobal(self._tip),
                self.digitTime(), 
                self
            )            
            
        if self._tb:
            self._tb.setText(self.digitTime())
      
        side = min(self.width(), self.height())
        time = QTime.currentTime()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(AnalogClock.hourColor)

        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(AnalogClock.hourHand)
        painter.restore()

        painter.setPen(AnalogClock.hourColor)

        for i in range(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(AnalogClock.minuteColor)

        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(AnalogClock.minuteHand)
        painter.restore()

        painter.setPen(AnalogClock.minuteColor)

        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(AnalogClock.secondColor)

        painter.save()
        painter.rotate(6.0 * time.second())
        painter.drawConvexPolygon(AnalogClock.secondHand)
        painter.restore()

        painter.setPen(AnalogClock.secondColor)

        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)

    def mouseDoubleClickEvent(self, mouseEvent):
        if mouseEvent.button() == Qt.RightButton:
            return
        elif mouseEvent.button() == Qt.MiddleButton:
            return
        else:
            self.alertDialog()
            return

    def wheelEvent(self, event):
        step = event.angleDelta()
        s = step.y()
        if s > 0:
            self.zoomin()
        else:
            if self.width() > 30:
                self.zommout()

    def zoomin(self):
        self.resize(self.width() * 1.1, self.height() * 1.1)

    def zommout(self):
        self.resize(self.width() * 0.9, self.height() * 0.9)

    def mousePressEvent(self, event):
        self.offset = event.pos()
        self._tip = None
        
        if self._alert:
            self._alert.close()
            
        if event.button() == Qt.RightButton:
            self.showDialog()
        if event.button() == Qt.MiddleButton:
            self.close()
        if event.button() == Qt.LeftButton:
            QApplication.setOverrideCursor(Qt.ClosedHandCursor)

    def mouseReleaseEvent(self, event):
        self._tip = event.pos()
        QApplication.restoreOverrideCursor()

    def enterEvent(self,event):
        self._tip = event.pos()
        QToolTip.showText(self.mapToGlobal(event.pos()),
                              self.digitTime(), self)            
        QApplication.setOverrideCursor(Qt.PointingHandCursor)

    def leaveEvent(self,event):
        self._tip = None
        QApplication.restoreOverrideCursor()
        
    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)
        
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    clock = AnalogClock()
    clock.show()
    sys.exit(app.exec_())
