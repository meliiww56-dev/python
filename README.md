專題名稱：[基本即時通訊系統]

作者: 翁明孝 - 11303308A、 高氏美川 - 11303313A、林柔均 - 11103109A、安玫俐 – 11303317A

專題簡介:
版本二雖然比極簡版稍長，但它清楚地帶出了報告中的三個關鍵技術點：
1.	架構 (Architecture): Client-Server。
2.	技術 (Protocol/Tool): Python TCP Socket。
3.	核心功能 (Core Function): 多連線管理 (Multi-client) 與廣播 (Broadcast)。
這樣評審或讀者能更快速地掌握專題的重點和難度。
功能特色:
- ✅ [功能1] 支援多個客戶端同時連接到單一伺服器。
- ✅ [功能2] 實現訊息即時廣播功能 (Real-time broadcast)。
- ✅ [功能3] 伺服器端採用多執行緒 (Threading) 技術，為每個客戶端連線獨立處理，確保 I/O 不阻塞。

系統架構
系統遵循標準的 Client-Server 模型。
組件 (Component)	描述 (Description)
伺服器 (Server)	監聽連線、管理所有活動客戶端的清單，並負責廣播訊息。使用多執行緒處理併發連線。
客戶端 (Client)	建立到伺服器的連線，允許使用者透過鍵盤發送訊息，並顯示從伺服器接收到的所有訊息。

協定設計
我們使用 TCP (Transmission Control Protocol) 作為底層傳輸層協定。
TCP: 提供 可靠 (Reliable) 且 有序 (Ordered) 的資料傳輸服務，非常適合需要確保訊息不遺失或錯序的文字聊天應用。

訊息格式
	編碼：UTF-8 文字字串 (String)
	客戶端 → 伺服器：使用者輸入的訊息
範例：
<img width="413" height="155" alt="image" src="https://github.com/user-attachments/assets/5e41ca8a-7b6a-4180-a699-e1e5dbf2a78d" />

	伺服器 → 客戶端（廣播）：在訊息前加上來源資訊 [IP:Port]
範例：
<img width="513" height="139" alt="image" src="https://github.com/user-attachments/assets/0aa2b261-39b6-45c5-b11a-1cd964fa9dfb" />

	回覆範例：
<img width="961" height="98" alt="image" src="https://github.com/user-attachments/assets/06fe0e4e-fb68-4678-8964-efa5644acab1" />
簡單、易解析、適合 terminal 即時聊天室使用。

安裝與執行
需求
•	Python 3.7 以上版本
•	無需額外套件，僅使用 Python 內建的 socket 與 threading 函式庫

安裝
1.	儲存檔案
•	將伺服器程式碼儲存為 chat_server.py
•	將客戶端程式碼儲存為 chat_client.py
•	確保兩個檔案在同一個資料夾中
2.	啟動伺服器
•	開啟第一個終端機 / CMD
<img width="548" height="127" alt="image" src="https://github.com/user-attachments/assets/c3287609-1cd6-4918-9b37-1ff30c492465" />

3.	啟動客戶端
•	開啟第二個（或更多）終端機 / CMD
<img width="541" height="133" alt="image" src="https://github.com/user-attachments/assets/09af339c-f269-4f86-9d0e-d2ed6b2af7dd" />

4.	測試系統
•	在任一客戶端輸入訊息並按 Enter
•	檢查訊息是否即時出現在所有其他客戶端

測試結果:
•	伺服器可同時接受多個 client 連線
•	所有 client 可即時接收廣播訊息
•	伺服器顯示廣播訊息及當前連線數
•	客戶端顯示訊息及來源 IP/Port







