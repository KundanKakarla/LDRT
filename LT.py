import streamlit as st
import pyrebase
from datetime import datetime
import base64

# ------------------------ Firebase Configuration ------------------------ #
firebaseConfig = {
    "apiKey": "AIzaSyB8QYglIoBIVccIbTr_bp9nGYB8Od7JOmQ",
    "authDomain": "ldr-tracker-6da52.firebaseapp.com",
    "databaseURL": "https://ldr-tracker-6da52-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "ldr-tracker-6da52",
    "storageBucket": "ldr-tracker-6da52.appspot.com",
    "messagingSenderId": "1063843236138",
    "appId": "1:1063843236138:web:cd1f63406602e222a93653",
    "measurementId": "G-RWRJ2H16KV"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

st.markdown(
    """
    <style>
    /* ---------------- Background Gradient ---------------- */
    .stApp {
        background: linear-gradient(135deg, #ffdde1, #ee9ca7, #cfd9df, #a1c4fd);
        background-size: 400% 400%;
        animation: gradientFlow 15s ease infinite;
        overflow: hidden;
    }

    @keyframes gradientFlow {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* ---------------- Starry Background ---------------- */
    .star {
        position: fixed;
        color: transparent;
        font-size: 18px;
        opacity: 0.8;
        animation: twinkle 5s infinite ease-in-out, floatUp 20s linear infinite, spin 10s linear infinite;
        filter: drop-shadow(0 0 6px rgba(255, 255, 255, 0.8));
        z-index: -1;
    }

    /* Twinkling effect */
    @keyframes twinkle {
        0% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.2); }
        100% { opacity: 0.3; transform: scale(1); }
    }

    /* Floating effect */
    @keyframes floatUp {
        from { transform: translateY(100vh); }
        to { transform: translateY(-10vh); }
    }

    /* Spinning effect */
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    /* Shooting star effect */
    .shooting-star {
        position: fixed;
        width: 100px;
        height: 2px;
        background: linear-gradient(-45deg, rgba(255,255,255,0.8), rgba(255,255,255,0));
        opacity: 0.8;
        transform: rotate(45deg);
        animation: shoot 5s linear infinite;
        z-index: -1;
    }

    @keyframes shoot {
        0% { top: 120%; left: -20%; opacity: 0; }
        10% { opacity: 1; }
        100% { top: -20%; left: 120%; opacity: 0; }
    }

    /* ---------------- Main block transparent ---------------- */
    .reportview-container, .main, .block-container {
        background: transparent;
    }

    /* ---------------- Text, Input, Label Colors ---------------- */
    .stTextInput > div > div > input, 
    .stSelectbox > div > div > select, 
    .stTextArea > div > textarea {
        background-color: #e3f2fd !important;
        color: #1565c0 !important;
        border: 2px solid #90caf9 !important;
        border-radius: 12px;
        text-transform: lowercase !important;
    }

    /* ---------------- File Uploader Styling ---------------- */
    .stFileUploader > div {
        background-color: #e3f2fd !important;
        color: #1565c0 !important;
        border: 2px dashed #90caf9 !important;
        border-radius: 12px;
        text-transform: lowercase !important;
    }

    /* ---------------- Button Colors ---------------- */
    .stButton > button {
        background-color: #64b5f6 !important;
        color: white !important;
        border: none;
        padding: 10px 20px;
        border-radius: 12px;
        font-weight: bold;
        transition: background-color 0.3s ease;
        text-transform: lowercase !important;
    }
    .stButton > button:hover {
        background-color: #42a5f5 !important;
        color: white !important;
    }

    /* ---------------- Scrollbar Cute Style ---------------- */
    ::-webkit-scrollbar {
        width: 12px;
    }
    ::-webkit-scrollbar-track {
        background: #bbdefb;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #64b5f6;
        border-radius: 20px;
        border: 3px solid #bbdefb;
    }

    /* ---------------- Headers and Text ---------------- */
    h1, h2, h3, h4, p, span, div, a {
        color: #0d47a1 !important;
        text-transform: lowercase !important;
    }
    </style>

    <!-- ---------------- Stars in Background ---------------- -->
    <div class="star" style="left: 10%; animation-duration: 18s; font-size: 18px; color: #fffacd;">✦</div>
    <div class="star" style="left: 20%; animation-duration: 22s; font-size: 22px; color: #ffecb3;">✧</div>
    <div class="star" style="left: 30%; animation-duration: 16s; font-size: 16px; color: #ffe0b2;">❇</div>
    <div class="star" style="left: 40%; animation-duration: 24s; font-size: 24px; color: #ffd180;">★</div>
    <div class="star" style="left: 50%; animation-duration: 20s; font-size: 20px; color: #fff59d;">✺</div>
    <div class="star" style="left: 60%; animation-duration: 19s; font-size: 19px; color: #ffcc80;">✦</div>
    <div class="star" style="left: 70%; animation-duration: 21s; font-size: 21px; color: #ffe082;">★</div>
    <div class="star" style="left: 80%; animation-duration: 23s; font-size: 23px; color: #ffab91;">❇</div>
    <div class="star" style="left: 90%; animation-duration: 17s; font-size: 17px; color: #ffccbc;">✧</div>

    <!-- ---------------- Shooting Stars ---------------- -->
    <div class="shooting-star" style="top: 20%; animation-delay: 0s;"></div>
    <div class="shooting-star" style="top: 40%; animation-delay: 2s;"></div>
    <div class="shooting-star" style="top: 60%; animation-delay: 4s;"></div>
    <div class="shooting-star" style="top: 80%; animation-delay: 6s;"></div>
    """,
    unsafe_allow_html=True
)



# ------------------------ Select User ------------------------ #
st.header("💖 Who's Writing Today?")
current_user = st.selectbox("Select your name", ["KK", "Tracy 🐼"])

# ------------------------ Welcome ------------------------ #
st.title(f"Welcome {current_user}'s LDR Tracker 💖")
st.write("Stay connected, share memories, track moods & dreams!")

# ------------------------ Relationship Summary ------------------------ #
all_entries = db.child("daily_entries").get()
date_key = datetime.now().strftime("%Y-%m-%d")

# Initialize summary counters
dates = [d.key() for d in all_entries.each()] if all_entries.each() else []
days_together = 0
days_not_together = 0
kk_active = 0
tracy_active = 0

for date in dates:
    entry = db.child("daily_entries").child(date).get().val()
    if entry:
        kk_filled = entry.get("KK", None)
        tracy_filled = entry.get("Tracy 🐼", None)

        if kk_filled:
            kk_active += 1
        if tracy_filled:
            tracy_active += 1
        if kk_filled and tracy_filled:
            days_together += 1
        else:
            days_not_together += 1

first_entry_date = datetime.strptime(min(dates), "%Y-%m-%d") if dates else datetime.now()

# ------------------------ Display Summary ------------------------ #
st.header("💞 Relationship Summary")
st.write(f"**Days Together (Both Active)**: {days_together} days")
st.write(f"**KK Active Days**: {kk_active} days")
st.write(f"**Tracy 🐼 Active Days**: {tracy_active} days")
st.write(f"**Days Not Together**: {days_not_together} days")
st.write(f"**Since**: {first_entry_date.strftime('%d %B, %Y')}")
st.write("---")

# ------------------------ Today's Memory ------------------------ #
st.header("🌸 Today's Memory")

mood = st.selectbox("How are you feeling today?", ["Happy 😊", "Sad 😔", "Angry 😡", "Normal 🙂"])
reason = st.text_input("Reason for feeling this way? (Optional)")

uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
caption = st.text_input("Caption for the memory")

# Bucket List
st.header("✨ Bucket List")
bucket_item = st.text_input("Add a bucket list item")
add_bucket = st.button("Add to Bucket List")
submit = st.button("Save Today's Entry")
# ------------------------ Display Bucket List (Organized with Checkmarks) ------------------------ #
st.header("✨ Bucket List")

# Fetch and organize bucket list items
bucket_list_data = db.child("bucket_list").get()
kk_bucket, tracy_bucket = [], []

if bucket_list_data.each():
    for item in bucket_list_data.each():
        item_data = item.val()
        added_by = item_data.get("added_by", "Unknown")
        complete_status = item_data.get("completed", False)
        item_text = item_data.get("item", "")

        # Organize based on user
        if added_by == "KK":
            kk_bucket.append({"id": item.key(), "item": item_text, "completed": complete_status})
        elif added_by == "Tracy 🐼":
            tracy_bucket.append({"id": item.key(), "item": item_text, "completed": complete_status})

# Display in columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("💙 KK's Bucket List")
    if kk_bucket:
        for b in kk_bucket:
            # Show checkbox with current status
            checked = st.checkbox(b["item"], value=b["completed"], key=b["id"])
            # Update status in real-time if changed
            if checked != b["completed"]:
                db.child("bucket_list").child(b["id"]).update({"completed": checked})
    else:
        st.write("No items added yet.")

with col2:
    st.subheader("💜 Tracy 🐼's Bucket List")
    if tracy_bucket:
        for b in tracy_bucket:
            # Show checkbox with current status
            checked = st.checkbox(b["item"], value=b["completed"], key=b["id"] + "_tracy")
            # Update status in real-time if changed
            if checked != b["completed"]:
                db.child("bucket_list").child(b["id"]).update({"completed": checked})
    else:
        st.write("No items added yet.")

# ------------------------ Firebase Handling ------------------------ #
if add_bucket and bucket_item:
    db.child("bucket_list").push({"item": bucket_item})
    st.success("Added to bucket list!")

if submit:
    data = {
        "mood": mood,
        "reason": reason if reason else "No reason provided",
        "caption": caption if caption else "No caption",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if uploaded_file:
        bytes_data = uploaded_file.read()
        encoded_image = base64.b64encode(bytes_data).decode()
        data["photo_base64"] = encoded_image
    else:
        data["photo_base64"] = None

    db.child("daily_entries").child(date_key).child(current_user).set(data)
    st.success("Your day has been saved! ❤️")

# ------------------------ Display Today's Memory ------------------------ #
# ------------------------ Display Today's Memory (Organized) ------------------------ #
st.header("📝 Today's Memories")

# Fetch today's entries for both KK and Tracy
today_entry_kk = db.child("daily_entries").child(date_key).child("KK").get().val()
today_entry_tracy = db.child("daily_entries").child(date_key).child("Tracy 🐼").get().val()

# Create 2 columns to display side by side
col1, col2 = st.columns(2)

# KK's Today's Memory
with col1:
    st.subheader("💙 KK's Memory")
    if today_entry_kk:
        st.write(f"**Mood:** {today_entry_kk['mood']}")
        st.write(f"**Reason:** {today_entry_kk['reason']}")
        st.write(f"**Caption:** {today_entry_kk['caption']}")
        if today_entry_kk["photo_base64"]:
            st.image(base64.b64decode(today_entry_kk["photo_base64"]), width=300)
        else:
            st.write("No photo uploaded")
    else:
        st.write("No entry for today yet! 🌸")

# Tracy's Today's Memory
with col2:
    st.subheader("💜 Tracy 🐼's Memory")
    if today_entry_tracy:
        st.write(f"**Mood:** {today_entry_tracy['mood']}")
        st.write(f"**Reason:** {today_entry_tracy['reason']}")
        st.write(f"**Caption:** {today_entry_tracy['caption']}")
        if today_entry_tracy["photo_base64"]:
            st.image(base64.b64decode(today_entry_tracy["photo_base64"]), width=300)
        else:
            st.write("No photo uploaded")
    else:
        st.write("No entry for today yet! 🌸")


# ------------------------ Display Past Memories ------------------------ #
# ------------------------ Display Past Memories (Organized) ------------------------ #
st.header("📅 Past Memories")

# Fetch latest 3 memories for each
kk_memories, tracy_memories = [], []

for date in sorted(dates, reverse=True):
    entry = db.child("daily_entries").child(date).get().val()
    if entry:
        if "KK" in entry and len(kk_memories) < 3:
            kk_memories.append((date, entry["KK"]))
        if "Tracy 🐼" in entry and len(tracy_memories) < 3:
            tracy_memories.append((date, entry["Tracy 🐼"]))
    if len(kk_memories) == 3 and len(tracy_memories) == 3:
        break

# Create 2 columns for KK and Tracy's past memories
col1, col2 = st.columns(2)

# KK's Past Memories
with col1:
    st.subheader("💙 KK's Past Memories")
    if kk_memories:
        for date, mem in kk_memories:
            st.markdown(f"**Date:** {date}")
            st.write(f"**Mood:** {mem['mood']}")
            st.write(f"**Reason:** {mem['reason']}")
            st.write(f"**Caption:** {mem['caption']}")
            if mem["photo_base64"]:
                st.image(base64.b64decode(mem["photo_base64"]), width=300)
            st.write("---")
    else:
        st.write("No memories from KK yet.")

# Tracy's Past Memories
with col2:
    st.subheader("💜 Tracy 🐼's Past Memories")
    if tracy_memories:
        for date, mem in tracy_memories:
            st.markdown(f"**Date:** {date}")
            st.write(f"**Mood:** {mem['mood']}")
            st.write(f"**Reason:** {mem['reason']}")
            st.write(f"**Caption:** {mem['caption']}")
            if mem["photo_base64"]:
                st.image(base64.b64decode(mem["photo_base64"]), width=300)
            st.write("---")
    else:
        st.write("No memories from Tracy 🐼 yet.")

