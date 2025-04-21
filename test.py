from browser_env import ScriptBrowserEnv, create_id_based_action
import time  # Optional: to slow things down for visibility

# Initialize environment
env = ScriptBrowserEnv(
    headless=False,
    observation_type="accessibility_tree",
    current_viewport_only=True,
    viewport_size={"width": 1280, "height": 720},
)

# Load OpenStreetMap config
config_file = "config_files/7.json"
obs, info = env.reset(options={"config_file": config_file})

# Build the type action string according to your format
element_id = 10
search_query = "New York"
enter_flag = 1  # Will press Enter after typing

# Construct the full action string
action_str = f"type [{element_id}] [{search_query}] [{enter_flag}]"
print(f"\nFormatted type action: {action_str}")

# Use the action creator to parse it and get the proper action object
action = create_id_based_action(action_str)

# Step with the type action
obs, reward, terminated, truncated, info = env.step(action)

# Optionally show results
print("\n--- Observation After Typing ---")
print(obs["text"][:1500])

# Optional: pause and close
time.sleep(1000)
env.close()
