Page({
  data: {
    userId: "student001",
    chatHistory: [],
    userInput: ""
  },

  onLoad() {},

  inputTyping(e) {
    this.setData({ userInput: e.detail.value });
  },

  sendMessage() {
    if (!this.data.userInput.trim()) return;

    const userMessage = this.data.userInput;
    this.setData({ userInput: "" });

    this.data.chatHistory.push({ role: "user", content: userMessage });
    this.setData({ chatHistory: this.data.chatHistory });

    wx.request({
      url: `${getApp().globalData.apiBaseUrl}/api/chat`,
      method: "POST",
      data: { user_id: this.data.userId, message: userMessage },
      success: (res) => {
        this.data.chatHistory.push({ role: "coach", content: res.data.reply });
        this.setData({ chatHistory: this.data.chatHistory });
      }
    });
  }
})
