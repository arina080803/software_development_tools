const vscode = require('vscode');
const { exec } = require('child_process');

function activate(context) {
  let disposable = vscode.commands.registerCommand('extension.formatPythonCode', function () {
    let editor = vscode.window.activeTextEditor;
    if (!editor) {
      return;
    }

    let document = editor.document;
    let filePath = document.fileName;

    if (document.languageId !== 'python') {
      vscode.window.showWarningMessage('This is not a Python file!');
      return;
    }

    exec(`autopep8 --in-place "${filePath}"`, (err, stdout, stderr) => {
      if (err) {
        vscode.window.showErrorMessage('Failed to format Python code: ' + stderr);
        return;
      }
      vscode.window.showInformationMessage('Python code formatted successfully!');
      document.save();
    });
  });

  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate
};
