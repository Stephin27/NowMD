def TC2():
    #Runs the "NowMDdemo" tested application.
    TestedApps.NowMDdemo.Run()
    #Enters 'User[Tab]' in the 'edLoginName' object.
    Aliases.NowMDdemo.formUserLogin.panelMain.panelLogin.edLoginName.Keys("User[Tab]")
    #Enters '123[Enter]' in the 'edPassword' object.
    Aliases.NowMDdemo.formUserLogin.panelMain.panelLogin.edPassword.Keys("123[Enter]")
    OCR.Recognize(Aliases.NowMDdemo.formMain.panelNavagation.NavPanel).BlockByText("Appointments").Click()
    Project.Variables.Var1.Reset()
    while not Project.Variables.Var1.IsEOF():
        OCR.Recognize(Aliases.NowMDdemo.formMain.panelNavagation.NavPanel.Window("TAdvNavBarPanel", "", 1).VCLObject("TRzToolButton")).BlockByText("appointment").Click()
        #Enters KeywordTests.TC2.Variables.Var1["Name"] in the 'edCode' object.
        Aliases.NowMDdemo.formAppointmentEntry.panelFields.gbPatient.edPatient.edCode.Keys(Project.Variables.Var1.Value.["Name"])
        #Clicks the 'sbNameSearch' object.
        Aliases.NowMDdemo.formAppointmentEntry.panelFields.gbPatient.edPatient.sbNameSearch.Click(8, 16)
        OCR.Recognize(Aliases.NowMDdemo.formSearchName.panelButtons.btnSelectName).BlockByText("Patient").Click()
        #Clicks the 'edName' object.
        Aliases.NowMDdemo.formAppointmentEntry.panelFields.gbPatient.edName.Click(89, 13)
        #Clicks the 'Window("TBtnWinControl")' object.
        Aliases.NowMDdemo.formAppointmentEntry.panelFields.gbPatient.VCLObject("lucReasonforVisit").Window("TBtnWinControl").Click(10, 13)
        OCR.Recognize(Aliases.NowMDdemo.Window("TwwPopupGrid", "", 1)).BlockByText("Appointment").Click()
        #Clicks the 'Window("TBtnWinControl")' object.
        Aliases.NowMDdemo.formAppointmentEntry.panelFields.gbPatient.VCLObject("lucResource").Window("TBtnWinControl").Click(9, 7)
        #Clicks the 'Window("TwwPopupGrid", "", 1)' object.
        Aliases.NowMDdemo.Window("TwwPopupGrid", "", 1).Click(61, 14)
        #Clicks the 'edNote' object.
        Aliases.NowMDdemo.formAppointmentEntry.panelFields.gbPatient.edNote.Click(60, 26)
        #Enters 'testing' in the 'edNote' object.
        Aliases.NowMDdemo.formAppointmentEntry.panelFields.gbPatient.edNote.Keys("testing")
        OCR.Recognize(Aliases.NowMDdemo.formAppointmentEntry.panelButtons.btnSave).BlockByText("Save").Click()
        Project.Variables.Var1.Next()
