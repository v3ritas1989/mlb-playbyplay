# mlb-playbyplay

This project aims to scrape play by play data from Baseball-Reference.com, a website dedicated to providing baseball player, team, and league statistics, as well as real-time play by play for each game. 


## Goal
The primary goal of this project is to learn web-scraping basics using Python in a community fashion. Please join the discussion on the [Python Scraping Discord channel](https://discord.gg/jYFkX9) where beginners such as myself work through problems and find solutions.

## Scope
The way I'd like to go about creating mlb-playbyplay is to start with realistic and obtainable objectives related to scraping play by play data from Baseball-Reference.com using Python. Based on [Discord community input](https://discord.gg/jYFkX9), if any, the scope may evolve into something more complex (and fun!), such as GUI interfaces, data analysis, etc.

## Objectives
 **1. Scrape play by play data from a specific game into a CSV.**
 
For this, why not start with something fun like [Game 7 of the 2017 World Series](https://www.baseball-reference.com/boxes/LAN/LAN201711010.shtml). The play by play data is one of the last tables on the page with the header **Play by play.** The following headers, along with associated data, should be exported to the CSV.
 
		| Inning | Score | Outs | Batting Team | Batter | Pitcher | wWPA | wWE | Play Description |
*NOTE: headers listed above vary slightly from headers on the website.*

 **2. Curate the data**
The data listed in the play by play table on Baseball-Reference.com is not ideal for data analysis. Examples include:

 - Inning is listed as T1 for top of first inning or B1 for bottom of first inning. It would be better to divide this field into two fields: **Inning Number** and **Inning Half**
 - Play description is not structured in a manner suitable for analysis. As is, it is currently a long string like so:  "Reached on E3 (throw) (Ground Ball to 2B-1B); Springer Scores/No RBI; Bregman to 2B". This could be divided into multiple fields such as **Out or Hit**, **Runs Batted In**, etc.

**3. Choose game of choice** 
After we are satisfied with scraping a single game, the next step is to expand the script to crawl any game of choice based on passed arguments: **playbyplay**(*home_team_abbreviation*, *date*)

## Python Version
I will be using Python 3.6
