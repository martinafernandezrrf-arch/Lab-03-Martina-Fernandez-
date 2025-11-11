import requests
import streamlit as st
import time

st.title("NBA API Data Explorer Test 🏀")

# Initalizes data list
if "listTeams" not in st.session_state:
    st.session_state.listTeams = []

def getTeamInfo():

    # listTeams is a list of tuples, each tuple corresponding to one team

    # Initializes progress bar
    progress = st.progress(0, text="Loading team data...")

    if st.session_state.listTeams == []:
        # Loop thru 30 id's starting from 1
        for i in range(1,31):
            specificTeamEndpoint = f"https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/{i}"
            specificTeamRequest = requests.get(specificTeamEndpoint)
            specificTeamData = specificTeamRequest.json()
        
            teamName = specificTeamData['team']['displayName']
            record = specificTeamData['team']['record']['items'][0]['summary']
            homeRecord = specificTeamData['team']['record']['items'][1]['summary']
            teamName = specificTeamData['team']['displayName']
            record = specificTeamData['team']['record']['items'][0]['summary']
            homeRecord = specificTeamData['team']['record']['items'][1]['summary']
            awayRecord = specificTeamData['team']['record']['items'][2]['summary']
            avgPointsAgainst = round(specificTeamData['team']['record']['items'][0]['stats'][2]['value'], 2)
            avgPointsFor = round(specificTeamData['team']['record']['items'][0]['stats'][3]['value'], 2)

            # Items in tuples are as below
            st.session_state.listTeams += [(teamName, record, homeRecord, awayRecord, avgPointsAgainst, avgPointsFor)]

            # Updates the progress bar once a team has its data loaded
            progress.progress(i/30, text=f"Loading team {i}/30...")

        # After finished, remove the progress bar and sort list
        progress.empty()    
        st.session_state.listTeams.sort()

getTeamInfo()


if not st.session_state.listTeams:
    st.error("Could not load team data.")
    st.stop()

st.subheader("Team Summary")

team_names = [team[0] for team in st.session_state.listTeams]
selected_team = st.selectbox("Select a team:", team_names)

for team in st.session_state.listTeams:
    if team[0] == selected_team:

        st.write(
            f"The {team[0]} are currently {team[1]}!"
        )
        st.write(
            f"Home record: {team[2]} | Away record: {team[3]}!"
        )
        st.write(
            f"Fun Fact: They score {team[5]} points per game on average "
            f"and allow {team[4]} points per game on average."
        )

st.subheader("Simple Stat Graph")

stat_choice = st.selectbox(
    "Choose a stat to graph:",
    ["Average Points For", "Average Points Against"]
)

num_teams = st.slider(
    "How many teams should be shown?",
    min_value = 5,
    max_value= len(st.session_state.listTeams),
    value=10
)

if stat_choice == "Average Points For":
    label = "Average Points For"
    values = [team[5] for team in st.session_state.listTeams[:num_teams]]

else:
    label = "Average Points Against"
    values = [team[4] for team in st.session_state.listTeams[:num_teams]]

st.subheader(f"{label} The First {num_teams} teams")
st.bar_chart(values)

st.write("Teams shown (left to right):")

for team in st.session_state.listTeams[:num_teams]:
    st.write("-",team[0])

    
def pageInitialize():

    # Display a spinner until getTeamInfo() is finished
    if st.session_state.listTeams == []:
        with st.spinner("Loading team data. This may take a few seconds"):
            getTeamInfo()

    # Display success message when getTeamInfo() is finished
    st.success("Data loaded successfully!")

def teamSummary():

    # Initialize temporary teamNames list
    teamNames = []

    # Adds teaNmames from listTeams
    for tuple in st.session_state.listTeams:
        teamNames += [tuple[0]]

    # Creates dropdown box to select a team based on teamNames
    selected_team = st.selectbox("Select a team:", teamNames)

    # Loops thru all tuples in listTeams
    for tuple in st.session_state.listTeams:

        # If the names match, display some information
        if tuple[0] == selected_team:
            st.write(f"The {tuple[0]} are currently {tuple[1]}. Their home record is {tuple[2]} while their away record is {tuple[3]}. They have conceded an average of {tuple[4]} points per game, while scoring an average of {tuple[5]} points per game.")
