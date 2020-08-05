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
        Aliases.NowMDdemo.formAppointmentEntry.panelFields.gbPatient.edPatient.edCode.Keys(Project.Variables.Var1.Value["Name"])
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

def TC4():
    #Double-clicks the 'MSTaskListWClass' object.
    Aliases.explorer.wndShell_TrayWnd.ReBarWindow32.MSTaskSwWClass.MSTaskListWClass.DblClick(261, 21)
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("https://demo.openmrs.org/openmrs/login.htm")
    #Sets the text 'admin' in the 'textboxUsername' text editor.
    Aliases.browser.pageLogin.textboxUsername.SetText("admin")
    #Enters '[Tab]' in the 'textboxUsername' object.
    Aliases.browser.pageLogin.textboxUsername.Keys("[Tab]")
    #Sets the text Project.Variables.Password1 in the 'passwordboxPassword' text editor.
    Aliases.browser.pageLogin.formLoginForm.fieldsetLogin.passwordboxPassword.SetText(Project.Variables.Password1)
    #Clicks the 'textnodeRegistrationDesk' object.
    Aliases.browser.pageLogin.formLoginForm.fieldsetLogin.textnodeRegistrationDesk.Click(97, 26)
    #Clicks the 'buttonLogIn' button.
    Aliases.browser.pageLogin.formLoginForm.fieldsetLogin.buttonLogIn.ClickButton()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageHome.Wait()
    #Clicks the 'buttonRegisterAPatient' button.
    Aliases.browser.pageHome.buttonRegisterAPatient.ClickButton()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageRegisterpatient.Wait()
    #Sets the text 'tom' in the 'textboxGivenRequired' text editor.
    Aliases.browser.pageRegisterpatient.formRegistration.textboxGivenRequired.SetText("tom")
    #Clicks the 'textboxFamilyNameRequired' object.
    Aliases.browser.pageRegisterpatient.textboxFamilyNameRequired.Click(76, 13)
    #Sets the text 'Harry' in the 'textboxFamilyNameRequired' text editor.
    Aliases.browser.pageRegisterpatient.textboxFamilyNameRequired.SetText("Harry")
    #Clicks the 'formRegistration' object.
    Aliases.browser.pageRegisterpatient.formRegistration.Click(119, 86)
    #Clicks the 'Male' item of the 'selectRequired' list box.
    Aliases.browser.pageRegisterpatient.formRegistration.selectRequired.ClickItem("Male")
    #Clicks the 'formRegistration' object.
    Aliases.browser.pageRegisterpatient.formRegistration.Click(104, 121)
    #Sets the text '27' in the 'textboxDay' text editor.
    Aliases.browser.pageRegisterpatient.formRegistration.textboxDay.SetText("27")
    #Enters '[Tab]' in the 'textboxDay' object.
    Aliases.browser.pageRegisterpatient.formRegistration.textboxDay.Keys("[Tab]")
    #Selects the 'January' item of the 'selectMonth' combo box.
    Aliases.browser.pageRegisterpatient.formRegistration.selectMonth.ClickItem("January")
    #Selects the 'February' item of the 'selectMonth' combo box.
    Aliases.browser.pageRegisterpatient.formRegistration.selectMonth.ClickItem("February")
    #Selects the 'March' item of the 'selectMonth' combo box.
    Aliases.browser.pageRegisterpatient.formRegistration.selectMonth.ClickItem("March")
    #Enters '[Tab]' in the 'selectMonth' object.
    Aliases.browser.pageRegisterpatient.formRegistration.selectMonth.Keys("[Tab]")
    #Sets the text '1980' in the 'textboxYear' text editor.
    Aliases.browser.pageRegisterpatient.formRegistration.textboxYear.SetText("1980")
    #Clicks the 'formRegistration' object.
    Aliases.browser.pageRegisterpatient.formRegistration.Click(144, 158)
    #Clicks the 'submitbuttonConfirm' button.
    Aliases.browser.pageRegisterpatient.formRegistration.submitbuttonConfirm.ClickButton()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageIndex.Wait()
