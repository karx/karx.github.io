https://forum.cursor.com/t/guide-5-steps-exporting-chats-prompts-from-cursor/2825
1. Go to workspaceStorage. (On Windows, `cd %APPDATA%\Cursor\User\workspaceStorage`)
2. You will see a list of folders whose names are md5 hashes. Open each of them.
3. `datasette state.vscdb`
4. Visit “[http://localhost:8001/state?](http://localhost:8001/state?)” in a browser and enter this query:

> SELECT  
> rowid,  
> [key],  
> value  
> FROM  
> ItemTable  
> WHERE  
> [key] IN (‘aiService.prompts’, ‘workbench.panel.aichat.view.aichat.chatdata’)

5. Parse the json based on your use case.

> [sheikheddy](https://forum.cursor.com/u/sheikheddy) 


Tools here:
* [[datasette]] https://docs.datasette.io/en/stable/installation.html#basic-installation