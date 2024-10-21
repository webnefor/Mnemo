# Mnemo

This app will help you learn the language. Research has shown that sometimes word pop-ups help you learn a word and add it to your active vocabulary. This application works as follows. By launching it, you specify the timer, after how many minutes the word will be shown to you, after that the application will work and select the word for you and after 10 seconds the translation, and then disappear. And so it will be cyclically repeated.

Example list.conf
    word,[pronunce],an example of using the word,translation;

Params:

  --time, -t 
  
      default: 1
      
  --path, -p 
  
      default: /words.list
      
  --mode, -m 
  
      default: 1 or 0
