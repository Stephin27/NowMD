def Test1():
    #Double-clicks the 'MSTaskListWClass' object.
    Aliases.explorer.wndShell_TrayWnd.ReBarWindow32.MSTaskSwWClass.MSTaskListWClass.DblClick(269, 10)
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("https://demo.openmrs.org/openmrs/login.htm")
    #Clicks the 'textboxUsername' object.
    Aliases.browser.pageLogin.textboxUsername.Click(226, 28)
    #Enters '^a' in the 'textboxUsername' object.
    Aliases.browser.pageLogin.textboxUsername.Keys("^a")
    #Sets the text 'admin' in the 'textboxUsername' text editor.
    Aliases.browser.pageLogin.textboxUsername.SetText("admin")
    #Enters '[Tab]' in the 'textboxUsername' object.
    Aliases.browser.pageLogin.textboxUsername.Keys("[Tab]")
    #Sets the text Project.Variables.Password1 in the 'passwordboxPassword' text editor.
    Aliases.browser.pageLogin.passwordboxPassword.SetText(Project.Variables.Password1)
    #Clicks the 'textnodeRegistrationDesk' object.
    Aliases.browser.pageLogin.formLoginForm.fieldsetLogin.textnodeRegistrationDesk.Click(44, 15)
    #Clicks the 'buttonLogIn' button.
    Aliases.browser.pageLogin.buttonLogIn.ClickButton()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageLogin.Wait()
    #Clicks the 'buttonRegisterAPatient' button.
    Aliases.browser.pageLogin.buttonRegisterAPatient.ClickButton()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageLogin.Wait()
    #Clicks the 'Logout' item of the 'nav' bar.
    Aliases.browser.pageLogin.nav.ClickItem("Logout")
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageLogin.Wait()
    #Closes the 'BrowserWindow' window.
    Aliases.browser.BrowserWindow.Close()
