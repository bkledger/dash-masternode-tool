# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/DMT-git/src/ui/ui_proposals.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProposalsDlg(object):
    def setupUi(self, ProposalsDlg):
        ProposalsDlg.setObjectName("ProposalsDlg")
        ProposalsDlg.resize(785, 505)
        ProposalsDlg.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProposalsDlg)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblMessage = QtWidgets.QLabel(ProposalsDlg)
        self.lblMessage.setText("")
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout.addWidget(self.lblMessage)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(ProposalsDlg)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(ProposalsDlg)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.propsView = QtWidgets.QTableView(self.splitter)
        self.propsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.propsView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.propsView.setAlternatingRowColors(True)
        self.propsView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.propsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.propsView.setShowGrid(True)
        self.propsView.setSortingEnabled(False)
        self.propsView.setObjectName("propsView")
        self.propsView.verticalHeader().setVisible(False)
        self.propsView.verticalHeader().setCascadingSectionResizes(False)
        self.propsView.verticalHeader().setHighlightSections(False)
        self.tabDetails = QtWidgets.QTabWidget(self.splitter)
        self.tabDetails.setObjectName("tabDetails")
        self.tabVoting = QtWidgets.QWidget()
        self.tabVoting.setObjectName("tabVoting")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabVoting)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabDetails.addTab(self.tabVoting, "")
        self.tabVoteList = QtWidgets.QWidget()
        self.tabVoteList.setObjectName("tabVoteList")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabVoteList)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.votesSplitter = QtWidgets.QSplitter(self.tabVoteList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.votesSplitter.sizePolicy().hasHeightForWidth())
        self.votesSplitter.setSizePolicy(sizePolicy)
        self.votesSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.votesSplitter.setObjectName("votesSplitter")
        self.layoutWidget = QtWidgets.QWidget(self.votesSplitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutVotesView = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layoutVotesView.setContentsMargins(0, 0, 0, 0)
        self.layoutVotesView.setSpacing(2)
        self.layoutVotesView.setObjectName("layoutVotesView")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnReloadVotes = QtWidgets.QPushButton(self.layoutWidget)
        self.btnReloadVotes.setObjectName("btnReloadVotes")
        self.horizontalLayout_2.addWidget(self.btnReloadVotes)
        self.chbOnlyMyVotes = QtWidgets.QCheckBox(self.layoutWidget)
        self.chbOnlyMyVotes.setToolTip("")
        self.chbOnlyMyVotes.setObjectName("chbOnlyMyVotes")
        self.horizontalLayout_2.addWidget(self.chbOnlyMyVotes)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.layoutVotesView.addLayout(self.horizontalLayout_2)
        self.layoutVotesViewFilter = QtWidgets.QHBoxLayout()
        self.layoutVotesViewFilter.setObjectName("layoutVotesViewFilter")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.layoutVotesViewFilter.addWidget(self.label_2)
        self.edtVotesViewFilter = QtWidgets.QLineEdit(self.layoutWidget)
        self.edtVotesViewFilter.setObjectName("edtVotesViewFilter")
        self.layoutVotesViewFilter.addWidget(self.edtVotesViewFilter)
        self.btnApplyVotesViewFilter = QtWidgets.QPushButton(self.layoutWidget)
        self.btnApplyVotesViewFilter.setObjectName("btnApplyVotesViewFilter")
        self.layoutVotesViewFilter.addWidget(self.btnApplyVotesViewFilter)
        self.layoutVotesView.addLayout(self.layoutVotesViewFilter)
        self.votesView = QtWidgets.QTableView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.votesView.sizePolicy().hasHeightForWidth())
        self.votesView.setSizePolicy(sizePolicy)
        self.votesView.setObjectName("votesView")
        self.layoutVotesView.addWidget(self.votesView)
        self.widget = QtWidgets.QWidget(self.votesSplitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_4.addWidget(self.votesSplitter)
        self.tabDetails.addTab(self.tabVoteList, "")
        self.tabWebPreview = QtWidgets.QWidget()
        self.tabWebPreview.setObjectName("tabWebPreview")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabWebPreview)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layoutWebPreview = QtWidgets.QVBoxLayout()
        self.layoutWebPreview.setObjectName("layoutWebPreview")
        self.layoutURL = QtWidgets.QHBoxLayout()
        self.layoutURL.setObjectName("layoutURL")
        self.label = QtWidgets.QLabel(self.tabWebPreview)
        self.label.setObjectName("label")
        self.layoutURL.addWidget(self.label)
        self.edtURL = QtWidgets.QLineEdit(self.tabWebPreview)
        self.edtURL.setReadOnly(True)
        self.edtURL.setObjectName("edtURL")
        self.layoutURL.addWidget(self.edtURL)
        self.layoutWebPreview.addLayout(self.layoutURL)
        self.verticalLayout_3.addLayout(self.layoutWebPreview)
        self.tabDetails.addTab(self.tabWebPreview, "")
        self.verticalLayout.addWidget(self.splitter)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProposalsDlg)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProposalsDlg)
        self.tabDetails.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ProposalsDlg)

    def retranslateUi(self, ProposalsDlg):
        _translate = QtCore.QCoreApplication.translate
        ProposalsDlg.setWindowTitle(_translate("ProposalsDlg", "Dialog"))
        self.pushButton.setText(_translate("ProposalsDlg", "Columns"))
        self.tabDetails.setTabText(self.tabDetails.indexOf(self.tabVoting), _translate("ProposalsDlg", "Voting && Details"))
        self.btnReloadVotes.setToolTip(_translate("ProposalsDlg", "Reads new votes from the Dash network"))
        self.btnReloadVotes.setText(_translate("ProposalsDlg", "Read new votes"))
        self.chbOnlyMyVotes.setText(_translate("ProposalsDlg", "Only my votes"))
        self.label_2.setText(_translate("ProposalsDlg", "Filter:"))
        self.btnApplyVotesViewFilter.setText(_translate("ProposalsDlg", "Apply"))
        self.tabDetails.setTabText(self.tabDetails.indexOf(self.tabVoteList), _translate("ProposalsDlg", "Vote List"))
        self.label.setText(_translate("ProposalsDlg", "URL: "))
        self.tabDetails.setTabText(self.tabDetails.indexOf(self.tabWebPreview), _translate("ProposalsDlg", "Webpage Preview"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProposalsDlg = QtWidgets.QDialog()
    ui = Ui_ProposalsDlg()
    ui.setupUi(ProposalsDlg)
    ProposalsDlg.show()
    sys.exit(app.exec_())

