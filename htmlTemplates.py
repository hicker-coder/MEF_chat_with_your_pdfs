css= """<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    font-family: 'Roboto', sans-serif;
    transition: transform 0.3s ease;
}

.chat-message.user {
    background-color: #1e1e1e;
    color: #fff;
}

.chat-message.bot {
    background-color: #2d333b;
    color: #fff;
}

.chat-message:hover {
    transform: scale(1.02);
}

.chat-message .avatar {
    width: 20%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.chat-message:hover .avatar img {
    transform: scale(1.1);
}

.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
    overflow-wrap: break-word;
}

/* Custom futuristic styles */
.chat-message.user::before,
.chat-message.bot::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 0;
    height: 100%;
    width: 3px;
    transform: translateY(-50%);
    background-color: #00ffff;
    transition: all 0.3s ease;
    opacity: 0;
}

.chat-message.user:hover::before,
.chat-message.bot:hover::before {
    opacity: 1;
    background-color: #0c64ff;
    width: 100%;
}

.chat-message.user .message,
.chat-message.bot .message {
    position: relative;
    z-index: 1;
}

.chat-message.user .message::before,
.chat-message.bot .message::before {
    content: '';
    position: absolute;
    bottom: -1rem;
    right: 1.5rem;
    height: 2px;
    width: 50%;
    background-color: #00ffff;
    transition: all 0.3s ease;
    opacity: 0;
}

.chat-message.user .message:hover::before,
.chat-message.bot .message:hover::before {
    opacity: 1;
    background-color: #0c64ff;
    width: 100%;
}

.chat-message.user .message::after,
.chat-message.bot .message::after {
    content: '';
    position: absolute;
    top: calc(50% - 6px);
    right: -9px;
    height: 12px;
    width: 12px;
    border-radius: 50%;
    background-color: #00ffff;
    transition: all 0.3s ease;
    opacity: 0;
}

.chat-message.user .message:hover::after,
.chat-message.bot .message:hover::after {
    opacity: 1;
    background-color: #0c64ff;
    transform: scale(1.3);
}
</style>
"""

bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://images.squarespace-cdn.com/content/v1/58f645cae58c62dbeca6bc2c/1532564876972-FWXTUJNYVNAQE045G346/SmartBot360+logo+-+square.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""


user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="question_mark.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
