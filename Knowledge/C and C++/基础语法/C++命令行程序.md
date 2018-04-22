# C++命令行程序

```
int main(int argc, char** argv)
{
	string cmd;
	while (1)
	{
		cout << "Please Input Command" << endl;
		getline(cin, cmd);
		if (cmd == "exit" || cmd == "quit" || cmd == "q")
		{
			cout << "exit ..." << endl;
			break;
		}
		else if (cmd == "...")
		{
			/* Do Something */
		}
		else
		{
		    cout << "Unknown command" << endl;
		}
	}
	return 0;
}
```
