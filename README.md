Here’s a clean and professional `README.md` you can use for your **TLS Decryption Project** repo. You can tweak names/paths as needed.

---

# 🔐 TLS Decryption Project

A hands-on project demonstrating how **TLS (Transport Layer Security)** works, including certificate generation, secure client-server communication, and traffic decryption using session keys.

---

## 📌 Overview

This project simulates a secure TLS connection between a client and a server. It covers:

* Creating a **Certificate Authority (CA)**
* Generating **server and client certificates**
* Establishing a **TLS-encrypted connection**
* Capturing and **decrypting TLS traffic** using session keys

---

## 🧠 Learning Objectives

* Understand how TLS handshake works
* Learn how certificates and trust chains are created
* Explore encryption/decryption in real scenarios
* Analyze TLS traffic using tools like Wireshark

---

## 🏗️ Project Structure

```
tls_project/
│
├── server/
│   ├── server.py
│   ├── server.crt
│   ├── server.key
│
├── client/
│   ├── client.py
│   ├── client.crt
│   ├── client.key
│
├── ca/
│   ├── ca.crt
│   ├── ca.key
│
├── ssl_keys.log
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Generate Certificate Authority (CA)

```bash
openssl genrsa -out ca.key 2048

openssl req -x509 -new -nodes -key ca.key -sha256 -days 365 \
-out ca.crt
```

---

### 2️⃣ Generate Server Certificate

```bash
openssl genrsa -out server.key 2048

openssl req -new -key server.key -out server.csr

openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key \
-CAcreateserial -out server.crt -days 365 -sha256
```

---

### 3️⃣ Generate Client Certificate

```bash
openssl genrsa -out client.key 2048

openssl req -new -key client.key -out client.csr

openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key \
-out client.crt -days 365 -sha256
```

---

## 🚀 Running the Project

### ▶️ Start Server

```bash
python3 server.py
```

---

### ▶️ Start Client

```bash
python3 client.py
```

---

## 🔍 TLS Decryption (Wireshark)

To decrypt TLS traffic:

### 1️⃣ Enable SSL Key Logging

```bash
export SSLKEYLOGFILE=~/tls_project/ssl_keys.log
```

---

### 2️⃣ Run Client Again

This will generate session keys inside:

```
ssl_keys.log
```

---

### 3️⃣ Configure Wireshark

* Go to:
  `Edit → Preferences → Protocols → TLS`

* Set:

```
(Pre)-Master-Secret log filename → ssl_keys.log
```

---

### 4️⃣ Analyze Traffic

Now you can:

* See decrypted HTTPS/TLS packets
* Inspect requests and responses
* Understand encryption flow

---

## 🛠️ Technologies Used

* Python (socket, ssl)
* OpenSSL
* Wireshark

---

## ⚠️ Notes

* Make sure ports (e.g., `4433`) are not already in use
* Ensure correct IP between client and server
* Certificates must match CA

---

## 📚 Future Improvements

* Add mutual TLS (mTLS)
* Implement certificate validation checks
* Automate certificate generation
* Add GUI for monitoring traffic

---

## 👨‍💻 Author

**Buger_Byte** – Cybersecurity Student
**Hemash** - Cybersecurity Student
Interested in TLS, Networking, and Offensive Security

---

## ⭐ Contribute

Feel free to fork, improve, and submit PRs!

---

