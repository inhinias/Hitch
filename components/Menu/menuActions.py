from PyQt5 import QtGui, QtCore, QtWidgets
from components import introductionWindow
from projectHandling import startupData

class MenuAction:
    selecedProject = ""

    #Menu file tab
    def newFile(self):
        print("new file")

    def openFile(self):
        print("open file")

    def openProjectFromFile(self):
        print("menuActions; MenuAction; openProjectFromFile: open project from file")
        self.filePath = QtWidgets.QFileDialog.getOpenFileName(self, "Open Project From File")
        if not(self.filePath[0] == ""):
            introductionWindow.Introduction.selectedProject = self.filePath[0]
            introductionWindow.Introduction.setProjectInfo(self, "fromFile")

    def selectProjectFolder(self):
        print("selecting project folder")
        self.selectFilePath = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder"))
        if not(self.selectFilePath == ""):
            self.selectFilePath += "/"
            introductionWindow.Introduction.selectedFolder = self.selectFilePath
            introductionWindow.Introduction.setProjectInfo(self, "fromCreate")
            introductionWindow.Introduction.appendProjectName(self)
            startupData.Data.storeTemp(self, "lastProjects", data=self.selectFilePath)

    def launchProject(self):
        print("menuActions; MenuAction; launchProject: Launching Project")
        intro = introductionWindow.Introduction
        #Check which tab was open and open the path.
        if intro.infoTabOpen:
            if intro.selectedProject != "":
                project = open(intro.selectedProject, "r+")
                project.close()
        
        else:
            if intro.selectedFolder != "" and intro.selectedProjectName != "":
                name = intro.selectedProjectName
                file = intro.selectedFolder
                project = open(file + name + ".hth", "w+")
                project.close()

            else:
                print(clr.Fore.RED + "menuActions; MenuAction; launchProject: Error launching project!")
                print(clr.Style.RESET_ALL + "Clearing colour marking!")

    def saveFile(self):
        print("save file")

    def saveAllFiles(self):
        print("save all files")

    def projectSettings(self):
        print("project settings")

    def editorSettings(self):
        print("editor settings")

    def switchProject(self):
        print("switch project")