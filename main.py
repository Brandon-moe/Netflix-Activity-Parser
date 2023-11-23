import pandas as pd
import os,sys

def main(user=None):
    #Load netflix activity file
    with open(os.path.join(os.getcwd(),"activity.csv"),"r",encoding="utf-8") as f:
        df = pd.read_csv(f)
    #filter by specified user
    if user:
        df = df[df["Profile Name"] == user]
    if df.empty:
        raise Exception("The provided user account could not be found in the data. Please check your spelling.")
    #extract series, season, and episode information from show entries
    df["Series"] = df["Title"].str.split(":").str[0]
    df["Season"] = df["Title"].str.split(":").str[1]
    df["Episode"] = df["Title"].str.split(":").apply(lambda x: ':'.join(x[2:]))
    #convert datetime columns to a datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Duration'] = pd.to_timedelta(df['Duration'])
    #discard any episodes that were watched for less than 5 minutes. These are
    #typically autoplays where the user didn't really watch the show, or the user
    #lost interest and clicked off quickly etc. not worth counting these.
    df = df[df['Duration'] > pd.Timedelta(minutes=5)]
    df = df.fillna('')
    #aggregate by series and only keep most recently watched episode
    idx = df.groupby('Series')['Start Time'].idxmax()
    df = df.loc[idx]
    #most recent activity at top of dataframe
    df = df.sort_values(by='Start Time',ascending=False)
    #filter out unneeded data and save to file
    df = df[["Series","Season","Episode"]]
    df.to_csv("output.csv", index=False)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
