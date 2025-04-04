# luredin_ctk.py (Revised Startup Logic v3 - No Withdraw/Deiconify)

# --- Imports ---
import customtkinter as ctk
import random
import math
from tkinter import messagebox
import json
import os

# -----------------------------------------------
# --- ALL GAME LOGIC HERE ---
# (LEVEL_PARAMS, comment lists, logic functions)
# --- Level params will be honorifics

LEVEL_PARAMS = {
    "Aspiring":     	{"range": (0, 9),     "max_eng": 10,  "pos_perc": 0.55, "swing": 2, "title": "Aspiring"},
    "Associate":	{"range": (10, 49),    "max_eng": 20,  "pos_perc": 0.60, "swing": 10, "title": "Associate"},
    "Professional":    	 {"range": (50, 99),    "max_eng": 40,  "pos_perc": 0.60, "swing": 50, "title": "Professional"},
    "Award Winning":       {"range": (100, 999),   "max_eng": 100, "pos_perc": 0.60, "swing": 100, "title": "Award Winning"},
    "Esteemed":        {"range": (1000, 9999),  "max_eng": 500, "pos_perc": 0.65, "swing": 1000, "title": "Esteemed"},
    "Honorable":         {"range": (10000, 99999),"max_eng": 2500,"pos_perc": 0.65, "swing": 10000, "title": "Honorable"},
    "Epic Legendary CEO":    {"range": (100000, 999999),"max_eng": 15000,"pos_perc": 0.70, "swing": 100000, "title": "Epic Legendary"},
    "G.O.A.T":           {"range": (1000000, float('inf')), "max_eng": 0, "pos_perc": 0.70, "swing": 0, "title": "G.O.A.T"}
}

# --- Positively Fake Comments ---- 
positive_comments_expanded = [
    "This resonates deeply!", "Couldn't agree more! 🙌", "Spot on! Exactly the kind of thinking we need.",
    "Well said! Adding this to my insights.", "So true! Important reminder. ✅", "Yes! This aligns perfectly with my perspective.",
    "Great point! Really makes you think.", "Love this energy! 🔥", "💯", "Absolutely nailed it.", "This is the validation I needed today. ✨",
    "This is fantastic! Keep sharing.", "Pure gold right here.", "Couldn't have put it better myself.", "Such a crucial point.",
    "Exactly! Elevating the conversation.", "On the money. 🎯", "This needs to be amplified!", "Yes, yes, and yes!", "In complete agreement.",
    "Insightful as always.", "Adding value with this post.", "This perspective is key.", "Mic drop moment. 🎤", "So much wisdom here.",
    "Keep shining! ✨", "Great contribution!", "This hits different. 👍", "Reposting this!", "This is going onto my vision board!"

#----  Negatively Negative Commments -LET'S DO THUS!!!--- 

]
negative_comments_expanded = [
    "Hmm, interesting perspective.", "Not sure I entirely follow the logic here.", "Is there data to back this up, or is it more of a feeling?",
    "Seems a bit... abstract?", "Okay, but what's the actionable takeaway?", "Respectfully disagree on this one.",
    "This feels familiar. Have seen similar posts.", "...", "Is this just common sense repackaged?", "Needs more substance, perhaps?",
    "I remain unconvinced.", "A bit too buzzword-heavy for me.", "Feels like corporate speak.", "Let's agree to disagree.",
    "Doesn't really land for me.", "Where's the 'how'?", "This is... certainly a take.", "Not seeing the novelty here.",
    "Seems reductionist.", "Easy to say, hard to implement.", "I think we can go deeper than this.", "Surface level, maybe?",
    "Is this universally applicable?", "Skeptical about the premise.", "Correlation or causation?", "Could be phrased more clearly.",
    "This adds nothing new.", "Circular reasoning?", "Bit of an echo chamber vibe?", "Do you have a link to the acrual study that these facts came from, or is this just your vibes?", "More derivative drivel from so-called experts"

]
lose_comment = "I wrote an article about how you're just generating these posts with AI"

# --- Logic Functions for vapid and banal titles ---
def get_player_level_info(followers):
    for title, params in LEVEL_PARAMS.items():
        min_f, max_f = params["range"];
        if min_f <= followers <= max_f: return title, params
    if followers >= 1_000_000: return "G.O.A.T", LEVEL_PARAMS["G.O.A.T"]
    return "Aspiring", LEVEL_PARAMS["Aspiring"]
def get_title_prefix(followers): _t, p = get_player_level_info(followers); return p["title"]
def generate_job_title():
    prefixes = ["Chief","Principal","Lead","Senior","Head of","Executive","Grand", "Grand Poobah", "Master"]
    actions = ["Synergy","Paradigm Shift","Disruption","Innovation","Alignment","Thought","Value","Impact","Growth", "Quality", "Vibe Engineering", "People", "Talent Acquisition"]
    roles = ["Evangelist","Architect","Ninja","Guru","Catalyst","Officer","Wizard","Champion", "Coach", "Mentor","Strategist","Smasher","Realization"]
    domains = ["of the Future","of Excellence","of Getting Things Done","of the Now","of Tomorrow's Promises","of Assumptions","of the Status Quo", "of Engagement"]
    parts = []; choice = random.random()
    if choice < 0.5: parts = [random.choice(prefixes), random.choice(actions), random.choice(roles), random.choice(domains)]
    elif choice < 0.8: parts = [random.choice(prefixes), random.choice(actions), random.choice(roles)]
    else: parts = [random.choice(actions), random.choice(roles), random.choice(domains)]
    return " ".join(parts)

#--- THE MOST BANAL AND VAPID POSTS HAVE A FORMULA AND A PATTERN -- 

def generate_luredin_post(topic):
    action_verbs = ["leverage","synergize","optimize","streamline","unpack","embrace","amplify","cultivate","ideate","disrupt","innovate","drive","empower", "lead", "manage", "develop", "design", "implement", "optimize", "coordinate", "orchestrate", "execute", "streamline",  
"engineer", "analyze", "resolve", "facilitate", "deliver", "enhance", "supervise", "collaborate", "mentor", "advise",  
"initiate", "launch", "innovate", "negotiate", "transform", "direct", "influence", "refine", "automate", "evaluate",  
"strategize", "create", "improve", "monitor", "assess", "document", "train", "test", "integrate", "debug"  ]
    nouns = ["strategy", "innovation", "synergy", "efficiency", "optimization", "scalability", "transformation", "framework", "roadmap", "architecture", "workflow", "paradigm", "ecosystem", "agility", "disruption", "integration", "alignment", "orchestration", "enablement", "leveraging", "visibility", "benchmarking", "analytics", "insights", "automation", "execution", "compliance", "governance", "differentiation", "growth", "engagement", "leadership", "impact", "velocity", "proficiency", "performance", "metrics", "value", "solution", "capability"]
    adjectives = ["holistic","impactful","scalable","authentic","proactive","agile","disruptive","client-centric","data-driven","forward-thinking","value-added", "scalable", "agile", "innovative", "strategic", "efficient", "dynamic", "cutting-edge", "synergistic", "data-driven", "customer-centric", "impactful", "proactive", "transformative", "best-in-class", "next-generation", "visionary", "cloud-based", "integrated", "streamlined", "high-performance", "optimized", "results-oriented", "cross-functional", "future-proof", "scalable", "best-practice", "customized", "adaptive",  
"robust", "proven", "versatile", "resilient", "empowered", "insightful", "actionable", "lean", "groundbreaking", "progressive"  ]
    adverbs = ["authentically","relentlessly","proactively","consistently","passionately", "genuinely", "strategically", "efficiently", "seamlessly", "proactively", "dynamically", "holistically", "effectively", "innovatively", "synergistically", "rapidly",  
"scalably", "agilely", "optimally"]
    concepts = ["the journey","the grind","continuous improvement","thinking outside the box","the bigger picture","core competency","low-hanging fruit","win-win situation", "taking a leap forward", "taking a leap backward", "fostering a learning culture", "stopping to smell the roses", "waking up to smell the java", "moving the needle", "leveraging synergies", "value creation", "leveling up", "pushing the envelope", "getting buy-in", "creating alignment",  
"navigating change", "building momentum", "unlocking potential", "driving impact", "embracing ambiguity", "the new normal", "circle back",  
"future-proofing the business", "hitting the ground running", "boiling the ocean", "leading with empathy", "walking the talk",  
"the art of the possible", "sailing uncharted waters", "the next big thing", "shifting the paradigm", "disrupting the status quo",  
"keeping a finger on the pulse", "bridging the gap", "raising the bar", "surfing the wave", "bringing it to the next level",  
"drilling down", "staying ahead of the curve", "putting people first", "coloring outside the lines", "leaning into uncertainty"  ]
    positive_affirmations = ["It's all about","Remember that","The key is","Never underestimate","Focus on", "It's like my grandma used to say", "My fortune cookie advised me that", "Shakespeare reminds us that it's better to love", "The wisdom of Albert Einstein reminds us that insanity is not doing enough"]
    vague_timeframes = ["moving forward","in today's landscape","going forward","this quarter","day in and day out", "this week", "In the coming fiscal year", "in our lifetime"]
    emojis = ["🚀","✨","💡","🙌","🔥","✅","➡️","💪","📈","💯"]
    hashtags = ["#motivation","#leadership","#innovation","#growthmindset","#futureofwork","#success","#inspiration","#thoughtleader","#hustle","#goals","#digitaltransformation","#personalbranding","#synergy", "#quality", "#softwaredevelopment", "#automation", "#empowerment" ]
    def get_ing_verb(): ing_verbs = ["leveraging","optimizing","streamlining","unpacking","embracing","amplifying","cultivating","ideating","disrupting","innovating","driving","empowering", "upskilling", "transforming", "enabling", "aligning", "synergizing", "scaling", "nurturing", "orchestrating", "accelerating", "reimagining", "facilitating", "mobilizing",  
"elevating", "redefining", "benchmarking", "monetizing", "enhancing", "curating", "fostering", "navigating", "expanding", "executing",  
"targeting", "connecting", "architecting", "personalizing", "revolutionizing", "adapting", "engaging", "streamlining", "delivering", "simplifying" ]; return random.choice(ing_verbs)
    templates = [
        lambda t: f"{random.choice(positive_affirmations)} {get_ing_verb()} the {random.choice(nouns)} around {t}. It's about {random.choice(adjectives)} {random.choice(nouns)} and {random.choice(adverbs)} {get_ing_verb()}!",
        lambda t: f"Let's unpack {t}. It’s not just a buzzword; it’s about {random.choice(adjectives)} {random.choice(nouns)} and {random.choice(concepts)}. {random.choice(vague_timeframes)}, we need to {random.choice(action_verbs)} our {random.choice(nouns)}.",
        lambda t: f"Deep dive on {t} today. {random.choice(positive_affirmations)} {random.choice(action_verbs)} your {random.choice(nouns)}. It's {random.choice(['the journey', 'the grind'])}. Stay {random.choice(adjectives)}!",
        lambda t: f"Thinking about {t} and its role in {random.choice(adjectives)} {random.choice(nouns)}. How are you {get_ing_verb()} {random.choice(nouns)} {random.choice(vague_timeframes)}? Let's {random.choice(action_verbs)} together! 👇",
        lambda t: f"{t.capitalize()}. That's the focus. {random.choice(action_verbs).capitalize()}. {random.choice(action_verbs).capitalize()}. {random.choice(action_verbs).capitalize()}. {random.choice(positive_affirmations)} results follow.",
        lambda t: f"Driving {random.choice(adjectives)} {random.choice(nouns)} through {t}. {random.choice(positive_affirmations)} {random.choice(concepts)} is key to {get_ing_verb()} {random.choice(nouns)}."]
    template = random.choice(templates); topic_clean = topic.strip(); post_text = template(topic_clean)
    rand_emoji = random.random(); ends_arrow = post_text.endswith("👇")
    if not ends_arrow:
        if rand_emoji < 0.10: post_text += f" {random.choice(emojis)} {random.choice(emojis)}"
        elif rand_emoji < 0.40: post_text += f" {random.choice(emojis)}"
    num_tags = random.randint(2, 3); chosen_tags = random.sample(hashtags, min(num_tags, len(hashtags)))
    if not ends_arrow and random.random() < 0.2 and "#thoughtleader" not in chosen_tags:
        if len(chosen_tags) < num_tags and chosen_tags: chosen_tags.append("#thoughtleader")
        elif chosen_tags: chosen_tags[0] = "#thoughtleader"
    post_text += " " + " ".join(chosen_tags); return post_text
def generate_luredin_comment(followers, lose):
    if lose: return lose_comment, "Negative"
    positive = random.random() < 0.60
    if positive: comment = random.choice(positive_comments_expanded); sentiment = "Positive"
    else: comment = random.choice(negative_comments_expanded); sentiment = "Negative"
    return comment, sentiment
def calculate_engagement_and_followers(followers):
    title_key, params = get_player_level_info(followers); lose = False
    likes=0; dislikes=0; pos_com=0; neg_com=0; comments_list=[]
    if title_key == "Epic Legendary" and followers >= 900000 and random.random() < 0.01:
        print("!!! AI Exposé Triggered !!!"); lose = True
        c_text, sent = generate_luredin_comment(followers, True); comments_list.append({"text": c_text, "sentiment": sent}); neg_com = 1
    else:
        max_eng = params["max_eng"]; base_pos = params["pos_perc"]
        num_com = random.randint(0, 10)
        min_ld = max(0, max_eng // 10) if max_eng > 0 else 0; max_ld = max(min_ld, max_eng)
        num_ld = random.randint(min_ld, max_ld) if max_ld > 0 else 0
        noisy_pos = max(0.0, min(1.0, base_pos + random.uniform(-0.05, 0.05)))
        for _ in range(num_com):
            c_text, sent = generate_luredin_comment(followers, False); comments_list.append({"text": c_text, "sentiment": sent})
            if sent == "Positive": pos_com += 1
            else: neg_com += 1
        for _ in range(num_ld):
            if random.random() < noisy_pos: likes += 1
            else: dislikes += 1
    net_pts = (likes * 1) + (pos_com * 5) - (dislikes * 1) - (neg_com * 5)
    max_swing = params["swing"]; f_change = 0
    if lose: f_change = -followers
    else:
        max_mag = (likes + dislikes) * 1 + (pos_com + neg_com) * 5
        if max_mag > 0: ratio = max(-1.0, min(1.0, net_pts / max_mag)); f_change = round(ratio * max_swing)
        f_change = max(f_change, -followers)
    return {"likes": likes, "dislikes": dislikes, "positive_comments": pos_com, "negative_comments": neg_com,
            "net_points": net_pts, "follower_change": f_change, "lose_condition_triggered": lose, "comments": comments_list}
def calculate_end_day_penalty_ceil(followers):
    if followers <= 0: return 0
    penalty = math.ceil(followers * 0.10); return min(penalty, followers)

# -----------------------------------------------
# --- END OF GAME LOGIC SECTION ---
# -----------------------------------------------

# --- Save/Load Functionality ---
# (save_game, load_game functions remain the same)
SAVE_FILE = "luredin_save.json"
def save_game(data):
    try:
        with open(SAVE_FILE, 'w') as f: json.dump(data, f, indent=4)
        print("Game saved successfully.")
    except Exception as e:
        print(f"Error saving game: {e}"); messagebox.showerror("Save Error", f"Could not save game progress:\n{e}")
def load_game():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r') as f: data = json.load(f)
            print("Save game loaded.")
            return data
        except Exception as e: print(f"Error loading save game: {e}"); return None
    else: print("No save file found."); return None

# --- Sign-in Screen Function ---
# (show_sign_in_screen function remains the same)
def show_sign_in_screen(main_app_instance):
    sign_in_window = ctk.CTkToplevel()
    sign_in_window.title("Become a LuredIn Legend!")
    sign_in_window.geometry("400x250")
    # Center the sign-in window relative to the (potentially invisible) main window
    # sign_in_window.update_idletasks() # Ensure dimensions are calculated
    # x = main_app_instance.winfo_rootx() + (main_app_instance.winfo_width() // 2) - (sign_in_window.winfo_width() // 2)
    # y = main_app_instance.winfo_rooty() + (main_app_instance.winfo_height() // 2) - (sign_in_window.winfo_height() // 2)
    # sign_in_window.geometry(f"+{x}+{y}") # Position it (optional)

    sign_in_window.transient(main_app_instance)
    sign_in_window.grab_set()
    sign_in_window.protocol("WM_DELETE_WINDOW", lambda: None)

    entered_name_var = ctk.StringVar()
    def on_submit():
        name = name_entry.get().strip()
        if name:
            entered_name_var.set(name)
            sign_in_window.grab_release()
            sign_in_window.destroy()
        else:
            error_label.configure(text="Error code ID 10-T:  A Thought Leader needs a name!", text_color="pink")

    title_label = ctk.CTkLabel(master=sign_in_window, text="Welcome, Aspiring Influencer!", font=("Helvetica", 16, "bold")); title_label.pack(pady=(20, 10))
    prompt_label = ctk.CTkLabel(master=sign_in_window, text="Craft your Thought Leader Moniker below:", wraplength=350); prompt_label.pack(pady=5)
    name_entry = ctk.CTkEntry(master=sign_in_window, placeholder_text="e.g., SynergySeeker_9000", width=250); name_entry.pack(pady=10); name_entry.focus()
    error_label = ctk.CTkLabel(master=sign_in_window, text="", text_color="pink"); error_label.pack(pady=5)
    submit_button = ctk.CTkButton(master=sign_in_window, text="Synergize My Profile!", command=on_submit); submit_button.pack(pady=20)
    name_entry.bind("<Return>", lambda event: on_submit())

    # This makes the script wait here until sign_in_window is destroyed, obliterated, ka-boom
    main_app_instance.wait_window(sign_in_window)
    return entered_name_var.get()


# --- Initialize Game State Variables (Defaults) ---
player_name = "Default Player"
followers = -1
base_job_title = "Default Title"
posts_today = 0
post_feed_data = []

# --- Create the main app instance FIRST ---
# --- DO NOT HIDE IT THIS TIME - ERMA GURD...---
app = ctk.CTk()

# --- Try Loading Game ---
loaded_data = load_game()

if loaded_data:
    # Use loaded data
    player_name = loaded_data.get("player_name", "Loaded Player")
    followers = loaded_data.get("followers", 0)
    base_job_title = loaded_data.get("base_job_title", generate_job_title())
    print(f"Welcome back, {player_name}!")
    # Proceed to setup main window below
else:
    # No save data, must show sign-in screen
    print("Proceeding to sign-in...")
    # The main 'app' window exists but might not be fully drawn yet.
    # show_sign_in_screen will appear on top and pause execution here.
    entered_name = show_sign_in_screen(app) # Pass the main app instance
    if entered_name:
        player_name = entered_name
    else:
        player_name = "Anon Influencer" # Fallback
        print("No name entered, using default.")
    # Initialize new game state
    followers = 0
    base_job_title = generate_job_title()
    print(f"Starting new game for {player_name}")
    # Proceed to setup main window below

# --- THE Main Window (after load/sign-in determined state) ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
app.title("LuredIn - Become the G.O.A.T.")
app.geometry("800x600")

# --- GUI ---
# ( widgets attached to 'app')
app.columnconfigure(0, weight=1, minsize=180); app.columnconfigure(1, weight=0); app.columnconfigure(2, weight=4)
app.rowconfigure(1, weight=1)
top_frame = ctk.CTkFrame(master=app, height=40, corner_radius=0); top_frame.grid(row=0, column=0, columnspan=3, padx=0, pady=0, sticky="ew")
luredin_label = ctk.CTkLabel(master=top_frame, text="LuredIn", font=("Helvetica", 16, "bold")); luredin_label.pack(side="left", padx=20, pady=5)
player_name_label_top = ctk.CTkLabel(master=app, text=f"Account: {player_name}", font=("Helvetica", 10)); player_name_label_top.pack(in_=top_frame, side="right", padx=20, pady=5)
left_frame = ctk.CTkFrame(master=app, width=180); left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew"); left_frame.grid_rowconfigure(3, weight=1)
player_name_label_left = ctk.CTkLabel(master=left_frame, text=player_name, font=("Helvetica", 12, "bold")); player_name_label_left.pack(pady=(10, 0))
job_title_label = ctk.CTkLabel(master=left_frame, text=f"{get_title_prefix(followers)} {base_job_title}", wraplength=160, justify="center"); job_title_label.pack(pady=5, padx=5)
follower_count_label = ctk.CTkLabel(master=left_frame, text=f"Followers: {followers:,}", font=("Helvetica", 14, "bold")); follower_count_label.pack(pady=10)
end_day_button = ctk.CTkButton(master=left_frame, text="My Work Is Done..."); end_day_button.pack(pady=20, side="bottom")
right_frame = ctk.CTkFrame(master=app); right_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew"); right_frame.columnconfigure(0, weight=1); right_frame.rowconfigure(3, weight=1)
input_label = ctk.CTkLabel(master=right_frame, text="Share your impactful vibes:"); input_label.grid(row=0, column=0, padx=10, pady=(10,0), sticky="w")
post_entry = ctk.CTkEntry(master=right_frame, placeholder_text="Enter topic..."); post_entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
button_frame = ctk.CTkFrame(master=right_frame, fg_color="transparent"); button_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
create_post_button = ctk.CTkButton(master=button_frame, text="🚀 Synthesize Post"); create_post_button.pack(side="left")
loading_label = ctk.CTkLabel(master=button_frame, text="", width=300); loading_label.pack(side="left", padx=10, fill='x', expand=True)
feed_frame = ctk.CTkScrollableFrame(master=right_frame, label_text="Feed"); feed_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")


# --- Action Functions (Callbacks) 
# (Make sure all handle_ functions are correctly defined here)
# def handle_create_post(): ...
# def handle_end_day(): ... (Remember it calls save_game)
# def update_profile_display(): ...
# def handle_read_comments(post_info, post_ui_frame, comments_button): ...
# def display_feed(): ...
def handle_create_post():
    global followers, posts_today, post_feed_data
    topic = post_entry.get()
    if not topic.strip(): loading_label.configure(text="Please enter a topic first!", text_color="pink"); return
    create_post_button.configure(state="disabled", text="Synthesizing...")
    loading_label.configure(text="Please wait while we generate engagement...", text_color=("black", "white"))
    app.update_idletasks()
    post_text = generate_luredin_post(topic)
    engagement_result = calculate_engagement_and_followers(followers)
    follower_change = engagement_result['follower_change']
    post_info = { "id": random.randint(1000, 9999), "text": post_text,
        "stats": f"👍{engagement_result['likes']} 👎{engagement_result['dislikes']} 💬{engagement_result['positive_comments']+engagement_result['negative_comments']}",
        "change": f"{follower_change:+}", "change_val": follower_change, "comments": engagement_result['comments'] }
    post_feed_data.insert(0, post_info)
    followers += follower_change; followers = max(0, followers); posts_today += 1
    post_entry.delete(0, "end"); loading_label.configure(text="")
    create_post_button.configure(state="normal", text="🚀 Synthesize Post")
    update_profile_display(); display_feed()
    if engagement_result['lose_condition_triggered']:
        messagebox.showerror("Game Over!", "🔥 YOU HAVE BEEN EXPOSED! 🔥\nYour AI-generated facade has crumbled. You lose all your followers!")
        followers = 0; update_profile_display(); create_post_button.configure(state="disabled"); end_day_button.configure(state="disabled")
    elif followers >= 1000000:
        messagebox.showinfo("You Won!", "🎉 A GOAT is YOU! 🎉\nCongratulations on reaching 1 Million Followers!")
        create_post_button.configure(state="disabled"); end_day_button.configure(state="disabled")

def handle_end_day():
    global followers, posts_today, player_name, base_job_title
    penalty = 0; message = "Your work is done for today. Vibes successfully managed."; title = "Day Ended"
    if posts_today == 0 and followers > 0:
        penalty = calculate_end_day_penalty_ceil(followers)
        followers -= penalty; followers = max(0, followers)
        message = f"You didn't post today and lost {penalty} followers!"; title = "Penalty!"
    messagebox.showinfo(title, message)
    posts_today = 0; update_profile_display()
    current_save_data = { "player_name": player_name, "followers": followers, "base_job_title": base_job_title }
    save_game(current_save_data)

def update_profile_display():
    follower_count_label.configure(text=f"Followers: {followers:,}")
    title_prefix = get_title_prefix(followers)
    job_title_label.configure(text=f"{title_prefix} {base_job_title}")
    player_name_label_top.configure(text=f"Account: {player_name}")
    player_name_label_left.configure(text=player_name)

def handle_read_comments(post_info, post_ui_frame, comments_button):
    if not post_info or not post_info.get("comments"): comments_button.configure(text="No Comments", state="disabled"); return
    comments_button.configure(state="disabled", text="Comments Shown")
    comments_area_frame = ctk.CTkFrame(master=post_ui_frame, fg_color="transparent"); comments_area_frame.pack(pady=(5, 5), padx=5, fill="x", anchor="w")
    header = ctk.CTkLabel(master=comments_area_frame, text="Comments:", font=("Segoe UI", 10, "italic")); header.pack(anchor="w", pady=(0,3))
    for comment_data in post_info["comments"]:
        text = comment_data.get("text", ""); sentiment = comment_data.get("sentiment", "Negative")
        if text == lose_comment: prefix = "🔥"; icon_color = "orange"
        elif sentiment == "Positive": prefix = "🟢"; icon_color = "green"
        else: prefix = "🔴"; icon_color = "red"
        comment_line_frame = ctk.CTkFrame(master=comments_area_frame, fg_color="transparent")
        comment_line_frame.pack(anchor="w", fill="x", padx=0, pady=0)
        icon_label = ctk.CTkLabel(master=comment_line_frame, text=prefix, text_color=icon_color, font=("Segoe UI", 10))
        icon_label.pack(side="left", padx=(5, 2), pady=0)
        text_label = ctk.CTkLabel(master=comment_line_frame, text=text, font=("Segoe UI", 10),
                                wraplength=max(100, post_ui_frame.winfo_width() - 50), justify="left" )
        text_label.pack(side="left", anchor='w', pady=0, fill='x', expand=True)

def display_feed():
    for widget in feed_frame.winfo_children(): widget.destroy()
    for post_info in post_feed_data:
        post_frame = ctk.CTkFrame(master=feed_frame, fg_color=("gray85", "gray20")); post_frame.pack(pady=8, padx=5, fill="x")
        post_text_widget = ctk.CTkTextbox(master=post_frame, corner_radius=0, border_width=0, activate_scrollbars=False); post_text_widget.insert("1.0", post_info['text'])
        lines = len(post_info['text']) / 50 + 1; height = min(max(int(lines * 18), 50), 200)
        post_text_widget.configure(state="disabled", height=height); post_text_widget.pack(pady=(5,0), padx=5, fill="x")
        stats_button_frame = ctk.CTkFrame(master=post_frame, fg_color="transparent"); stats_button_frame.pack(pady=2, padx=5, fill="x", anchor="w")
        stats_label = ctk.CTkLabel(master=stats_button_frame, text=post_info['stats'], font=("Segoe UI", 10)); stats_label.pack(side="left")
        change_color = "green" if post_info['change_val'] >= 0 else "red"
        change_label = ctk.CTkLabel(master=stats_button_frame, text=f"Followers: {post_info['change']}", text_color=change_color, font=("Segoe UI", 10, "bold")); change_label.pack(side="left", padx=10)
        comments_button = ctk.CTkButton( master=stats_button_frame, text="Read Comments", width=110, height=20, font=("Segoe UI", 10) )
        comments_button.configure(command=lambda pi=post_info, pf=post_frame, cb=comments_button: handle_read_comments(pi, pf, cb)); comments_button.pack(side="right", padx=5)

# --- Assign Commands to Buttons ---
create_post_button.configure(command=handle_create_post)
end_day_button.configure(command=handle_end_day)

# --- Initial Display Setup ---
# Update the display based on the final state determined above
update_profile_display()
display_feed()

# --- Run the Application ---
# Start the event loop for the main window 'app'
# It should become visible and interactive here.
app.mainloop()