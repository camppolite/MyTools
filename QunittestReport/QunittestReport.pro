#-------------------------------------------------
#
# Project created by QtCreator 2017-12-08T15:37:07
#
#-------------------------------------------------
QT += core
QT -= gui

CONFIG += c++11

TARGET = QunittestReport
CONFIG += console
CONFIG -= app_bundle

TEMPLATE = app

SOURCES += main.cpp

include($$PWD/../../../include/global.prf)

DEFINES += SRCDIR=\\\"$$PWD/\\\"

DESTDIR = $$BIN_DIR

template.files += $$PWD/project_template/*
template.path = $$BIN_DIR/

INSTALLS += template
