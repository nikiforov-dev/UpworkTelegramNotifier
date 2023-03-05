# Preparations
1. Download [chromedriver](https://sites.google.com/chromium.org/driver/downloads) suitable for your chrome version 
2. Unzip chromedriver and place it inside **driver** directory
3. Create Bot via BotFather
4. Create Channel
5. Add bot to channel administrators
6. Do such request in browser https://api.telegram.org/bot{{TOKEN}}/getUpdates with {{TOKEN}} replaced by your bot token
7. Send something in your channel
8. Repeat request #6 and get "id" from response
9. Insert conversation id into config.ini