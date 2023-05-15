
# unSwearNow

Same idea as [unSwear by mhavelka77](https://github.com/mhavelka77/unSwear), but replace instantly each word.  
  
After testing unSwear, i found it unfortunate that you should press space bar each time to confirm the word replacement.   
  
Sometimes you write an insult at the end of your message, and with unSwear, it doesnt replace the toxic word. With this version, no matter how/where you write, it will replace the cuss word.

## Filter

The filter operation is nearly the same as unSwear, just a few changes :  
- The file is a `.txt` file and not a `.csv`.
- The bad words/good words separator is a `=`.
- You can sequence the filter file by language.  
  
If it is likely that you speak more than one language in chat, make a new line, add a `#` before the new language you wanna file (ex: `# english`), and then write every replacement you want to have !

## Requirements 

Just need to install `pynput` module (same as unSwear).  
  
You can do it by typing `pip install pynput` in console command (with python already installed).
