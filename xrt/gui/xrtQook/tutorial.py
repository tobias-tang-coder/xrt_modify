﻿# -*- coding: utf-8 -*-
u"""
.. _qook_tutorial:

Using xrtQook for script generation
-----------------------------------

- Start xrtQook: type ``python xrtQook.pyw`` from xrt/xrtQook or, if you have
  installed xrt by running setup.py, type ``xrtQook.pyw`` from any location.

  .. note::
     If you want to start xrtQook from Spyder, select the run option
     "Execute in an external system terminal".

- Rename beamLine to myTestBeamline by double clicking on it (you do not have
  to, only for demonstration).

- Right-click on myTestBeamline and Add Source → BendingMagnet. The same can be
  done from the icon buttons on the left.

  .. imagezoom:: _images/qookTutor1.png
     :scale: 60 %

- In its properties change eMin to 10000-1 and eMax to 10000+1. The middle of
  this range will be used to automatically align crystals (one crystal in this
  example). Blue color indicates non-default values. These will be included
  into the generated script. All the default-valued parameters do not propagate
  into the script.

  .. imagezoom:: _images/qookTutor2.png
     :scale: 60 %

- Create a crystalline material CrystalSi. This will create a Si111 crystal at
  room temperature.

  .. imagezoom:: _images/qookTutor3.png
     :scale: 60 %

- Add a generic OE -> OE. This will add an optical element with a flat surface.

  .. note::
     The sequence of the inserted optical elements does matter! This sequence
     determines the order of beam propagation.

  .. imagezoom:: _images/qookTutor4.png
     :scale: 60 %

- In its properties select the created crystal as 'material', put [0, 20000, 0]
  as 'center' (i.e. 20 m from source) and "auto" (with or without quotes) as
  'pitch'.

  .. imagezoom:: _images/qookTutor5.png
     :scale: 60 %

- Add a screen to the beamline.

  .. imagezoom:: _images/qookTutor6.png
     :scale: 60 %

- Give it [0, 21000, auto] as 'center'. Its height -- the last coordinate --
  will be automatically calculated from the previous elements.

  .. imagezoom:: _images/qookTutor7.png
     :scale: 60 %

- Add a plot and select the local screen beam.

  .. imagezoom:: _images/qookTutor8.png
     :scale: 60 %

- Define an offset to the color (energy) axis.

  .. imagezoom:: _images/qookTutor9.png
     :scale: 60 %

- Save the beamline layout as xml.

- Generate python script (the button with a code page and the python logo),
  save the script and run it.

- In the console output you can read the actual pitch (Bragg angle) for the
  crystal and the screen position.

  .. imagezoom:: _images/qookTutorL.png
     :scale: 60 %

"""
