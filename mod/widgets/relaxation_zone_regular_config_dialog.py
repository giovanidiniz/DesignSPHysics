#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""DesignSPHysics Relaxation Zone Regular Config Dialog. """

# from PySide import QtGui
from PySide6 import QtWidgets

from mod.translation_tools import __

from mod.dataobjects.relaxation_zone_regular import RelaxationZoneRegular


class RelaxationZoneRegularConfigDialog(QtWidgets.QDialog):
    """ A configuration dialog for a regular relaxation zone. """

    def __init__(self, relaxationzone=None, parent=None):
        super().__init__(parent=parent)
        self.temp_relaxationzone = relaxationzone if relaxationzone is not None else RelaxationZoneRegular()
        self.relaxationzone = relaxationzone

        self.main_layout = QtWidgets.QVBoxLayout()
        self.data_layout = QtWidgets.QVBoxLayout()
        self.button_layout = QtWidgets.QHBoxLayout()

        self.start_layout = QtWidgets.QHBoxLayout()
        self.start_label = QtWidgets.QLabel(__("Start time (s):"))
        self.start_input = QtWidgets.QLineEdit()
        for x in [self.start_label, self.start_input]:
            self.start_layout.addWidget(x)

        self.duration_layout = QtWidgets.QHBoxLayout()
        self.duration_label = QtWidgets.QLabel(__("Movement duration (0 for end of simulation):"))
        self.duration_input = QtWidgets.QLineEdit()
        for x in [self.duration_label, self.duration_input]:
            self.duration_layout.addWidget(x)

        self.waveorder_layout = QtWidgets.QHBoxLayout()
        self.waveorder_label = QtWidgets.QLabel(__("Order wave generation:"))
        self.waveorder_input = QtWidgets.QLineEdit()
        for x in [self.waveorder_label, self.waveorder_input]:
            self.waveorder_layout.addWidget(x)

        self.waveheight_layout = QtWidgets.QHBoxLayout()
        self.waveheight_label = QtWidgets.QLabel(__("Wave Height:"))
        self.waveheight_input = QtWidgets.QLineEdit()
        for x in [self.waveheight_label, self.waveheight_input]:
            self.waveheight_layout.addWidget(x)

        self.waveperiod_layout = QtWidgets.QHBoxLayout()
        self.waveperiod_label = QtWidgets.QLabel(__("Wave Period:"))
        self.waveperiod_input = QtWidgets.QLineEdit()
        for x in [self.waveperiod_label, self.waveperiod_input]:
            self.waveperiod_layout.addWidget(x)

        self.depth_layout = QtWidgets.QHBoxLayout()
        self.depth_label = QtWidgets.QLabel(__("Water depth:"))
        self.depth_input = QtWidgets.QLineEdit()
        for x in [self.depth_label, self.depth_input]:
            self.depth_layout.addWidget(x)

        self.swl_layout = QtWidgets.QHBoxLayout()
        self.swl_label = QtWidgets.QLabel(__("Still water level:"))
        self.swl_input = QtWidgets.QLineEdit()
        for x in [self.swl_label, self.swl_input]:
            self.swl_layout.addWidget(x)

        self.center_layout = QtWidgets.QHBoxLayout()
        self.center_label = QtWidgets.QLabel(__("Central point (X, Y, Z):"))
        self.center_x = QtWidgets.QLineEdit()
        self.center_y = QtWidgets.QLineEdit()
        self.center_z = QtWidgets.QLineEdit()
        for x in [self.center_label, self.center_x, self.center_y, self.center_z]:
            self.center_layout.addWidget(x)

        self.width_layout = QtWidgets.QHBoxLayout()
        self.width_label = QtWidgets.QLabel(__("Width for generation:"))
        self.width_input = QtWidgets.QLineEdit()
        for x in [self.width_label, self.width_input]:
            self.width_layout.addWidget(x)

        self.phase_layout = QtWidgets.QHBoxLayout()
        self.phase_label = QtWidgets.QLabel(__("Initial wave phase:"))
        self.phase_input = QtWidgets.QLineEdit()
        for x in [self.phase_label, self.phase_input]:
            self.phase_layout.addWidget(x)

        self.ramp_layout = QtWidgets.QHBoxLayout()
        self.ramp_label = QtWidgets.QLabel(__("Periods of ramp:"))
        self.ramp_input = QtWidgets.QLineEdit()
        for x in [self.ramp_label, self.ramp_input]:
            self.ramp_layout.addWidget(x)

        self.savemotion_layout = QtWidgets.QHBoxLayout()
        self.savemotion_label = QtWidgets.QLabel(__("Save motion data ->"))
        self.savemotion_periods_label = QtWidgets.QLabel(__("Periods: "))
        self.savemotion_periods_input = QtWidgets.QLineEdit()
        self.savemotion_periodsteps_label = QtWidgets.QLabel(__("Period steps: "))
        self.savemotion_periodsteps_input = QtWidgets.QLineEdit()
        self.savemotion_xpos_label = QtWidgets.QLabel(__("X Position: "))
        self.savemotion_xpos_input = QtWidgets.QLineEdit()
        self.savemotion_zpos_label = QtWidgets.QLabel(__("Z Position: "))
        self.savemotion_zpos_input = QtWidgets.QLineEdit()
        for x in [self.savemotion_label,
                  self.savemotion_periods_label,
                  self.savemotion_periods_input,
                  self.savemotion_periodsteps_label,
                  self.savemotion_periodsteps_input,
                  self.savemotion_xpos_label,
                  self.savemotion_xpos_input,
                  self.savemotion_zpos_label,
                  self.savemotion_zpos_input]:
            self.savemotion_layout.addWidget(x)

        self.coefdir_layout = QtWidgets.QHBoxLayout()
        self.coefdir_label = QtWidgets.QLabel(__("Coefficient for each direction (X, Y, Z):"))
        self.coefdir_x = QtWidgets.QLineEdit()
        self.coefdir_x.setEnabled(False)
        self.coefdir_y = QtWidgets.QLineEdit()
        self.coefdir_y.setEnabled(False)
        self.coefdir_z = QtWidgets.QLineEdit()
        self.coefdir_z.setEnabled(False)
        for x in [self.coefdir_label, self.coefdir_x, self.coefdir_y, self.coefdir_z]:
            self.coefdir_layout.addWidget(x)

        self.coefdt_layout = QtWidgets.QHBoxLayout()
        self.coefdt_label = QtWidgets.QLabel(__("Multiplier for dt value in each direction:"))
        self.coefdt_input = QtWidgets.QLineEdit()
        self.coefdt_input.setEnabled(False)
        for x in [self.coefdt_label, self.coefdt_input]:
            self.coefdt_layout.addWidget(x)

        self.function_layout = QtWidgets.QHBoxLayout()
        self.function_label = QtWidgets.QLabel(__("Coefficients in function for velocity ->"))
        self.function_psi_label = QtWidgets.QLabel(__("Psi: "))
        self.function_psi_input = QtWidgets.QLineEdit()
        self.function_beta_label = QtWidgets.QLabel(__("Beta: "))
        self.function_beta_input = QtWidgets.QLineEdit()
        for x in [self.function_label,
                  self.function_psi_label,
                  self.function_psi_input,
                  self.function_beta_label,
                  self.function_beta_input]:
            self.function_layout.addWidget(x)

        self.driftcorrection_layout = QtWidgets.QHBoxLayout()
        self.driftcorrection_label = QtWidgets.QLabel(__("Coefficient of drift correction (for X):"))
        self.driftcorrection_input = QtWidgets.QLineEdit()
        for x in [self.driftcorrection_label, self.driftcorrection_input]:
            self.driftcorrection_layout.addWidget(x)

        for x in [self.start_layout,
                  self.duration_layout,
                  self.waveorder_layout,
                  self.waveheight_layout,
                  self.waveperiod_layout,
                  self.depth_layout,
                  self.swl_layout,
                  self.center_layout,
                  self.width_layout,
                  self.phase_layout,
                  self.ramp_layout,
                  self.savemotion_layout,
                  self.coefdir_layout,
                  self.coefdt_layout,
                  self.function_layout,
                  self.driftcorrection_layout]:
            self.data_layout.addLayout(x)

        self.delete_button = QtWidgets.QPushButton(__("Delete RZ configuration"))
        self.apply_button = QtWidgets.QPushButton(__("Apply this configuration"))
        self.button_layout.addStretch(1)
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addWidget(self.apply_button)

        self.main_layout.addLayout(self.data_layout)
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.button_layout)
        self.apply_button.clicked.connect(self.on_apply)
        self.delete_button.clicked.connect(self.on_delete)
        self.setLayout(self.main_layout)
        self.fill_data()
        self.exec_()

    def on_apply(self):
        """ Saves the current dialog data into the data structure. """
        self.temp_relaxationzone.start = float(self.start_input.text())
        self.temp_relaxationzone.duration = float(self.duration_input.text())
        self.temp_relaxationzone.waveorder = float(self.waveorder_input.text())
        self.temp_relaxationzone.waveheight = float(self.waveheight_input.text())
        self.temp_relaxationzone.waveperiod = float(self.waveperiod_input.text())
        self.temp_relaxationzone.depth = float(self.depth_input.text())
        self.temp_relaxationzone.swl = float(self.swl_input.text())
        self.temp_relaxationzone.center[0] = float(self.center_x.text())
        self.temp_relaxationzone.center[1] = float(self.center_y.text())
        self.temp_relaxationzone.center[2] = float(self.center_z.text())
        self.temp_relaxationzone.width = float(self.width_input.text())
        self.temp_relaxationzone.phase = float(self.phase_input.text())
        self.temp_relaxationzone.ramp = float(self.ramp_input.text())
        self.temp_relaxationzone.savemotion_periods = float(self.savemotion_periods_input.text())
        self.temp_relaxationzone.savemotion_periodsteps = float(self.savemotion_periodsteps_input.text())
        self.temp_relaxationzone.savemotion_xpos = float(self.savemotion_xpos_input.text())
        self.temp_relaxationzone.savemotion_zpos = float(self.savemotion_zpos_input.text())
        self.temp_relaxationzone.coefdir[0] = float(self.coefdir_x.text())
        self.temp_relaxationzone.coefdir[1] = float(self.coefdir_y.text())
        self.temp_relaxationzone.coefdir[2] = float(self.coefdir_z.text())
        self.temp_relaxationzone.coefdt = float(self.coefdt_input.text())
        self.temp_relaxationzone.function_psi = float(self.function_psi_input.text())
        self.temp_relaxationzone.function_beta = float(self.function_beta_input.text())
        self.temp_relaxationzone.driftcorrection = float(self.driftcorrection_input.text())
        self.relaxationzone = self.temp_relaxationzone
        self.accept()

    def on_delete(self):
        """ Deletes the currently represented relaxation zone. """
        self.relaxationzone = None
        self.reject()

    def fill_data(self):
        """ Fills the data from the data structure onto the dialog. """
        self.start_input.setText(str(self.temp_relaxationzone.start))
        self.duration_input.setText(str(self.temp_relaxationzone.duration))
        self.waveorder_input.setText(str(self.temp_relaxationzone.waveorder))
        self.waveheight_input.setText(str(self.temp_relaxationzone.waveheight))
        self.waveperiod_input.setText(str(self.temp_relaxationzone.waveperiod))
        self.depth_input.setText(str(self.temp_relaxationzone.depth))
        self.swl_input.setText(str(self.temp_relaxationzone.swl))
        self.center_x.setText(str(self.temp_relaxationzone.center[0]))
        self.center_y.setText(str(self.temp_relaxationzone.center[1]))
        self.center_z.setText(str(self.temp_relaxationzone.center[2]))
        self.width_input.setText(str(self.temp_relaxationzone.width))
        self.phase_input.setText(str(self.temp_relaxationzone.phase))
        self.ramp_input.setText(str(self.temp_relaxationzone.ramp))
        self.savemotion_periods_input.setText(str(self.temp_relaxationzone.savemotion_periods))
        self.savemotion_periodsteps_input.setText(str(self.temp_relaxationzone.savemotion_periodsteps))
        self.savemotion_xpos_input.setText(str(self.temp_relaxationzone.savemotion_xpos))
        self.savemotion_zpos_input.setText(str(self.temp_relaxationzone.savemotion_zpos))
        self.coefdir_x.setText(str(self.temp_relaxationzone.coefdir[0]))
        self.coefdir_y.setText(str(self.temp_relaxationzone.coefdir[1]))
        self.coefdir_z.setText(str(self.temp_relaxationzone.coefdir[2]))
        self.coefdt_input.setText(str(self.temp_relaxationzone.coefdt))
        self.function_psi_input.setText(str(self.temp_relaxationzone.function_psi))
        self.function_beta_input.setText(str(self.temp_relaxationzone.function_beta))
        self.driftcorrection_input.setText(str(self.temp_relaxationzone.driftcorrection))
