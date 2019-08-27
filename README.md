Copyright 2019, Kaito Yamagishi, all rights reserved

## TilT Documentation

#### **Problem Statement**

- Currently no smartphone/web application(s) support live mapping for the MBTA in a simple and intuitive manner

> I have used both of these services myself, and have great respect towards the developer of these applications. Just wanted to make something new that didn't exist that fits my preferences, not neccesairly better.

- Example 1: Live MBTA Subway Mapping by Stefan!
  - By using Google Maps, this web app gets clogged up easily
  - Screen looks very busy and not simple
  - Very hard to use on smartphone: but target users for this service is smartphone users (more likely to check live information on the go)
- Example 2: ProximiT
  - Great UI, easy to use, but only shows minutes
  - A display of only time can be frustrating for some users: we want location of the vehicles

#### **Solution (Test Checklist)**

- [x] An web page/application that provides a simple, intuitive view of the T's current location
- [x] Start from Green Line B, might develop for more lines
- [x] Users select a stop to view the station and its surrounding stations/trains
- [x] Show +- 2 stops from the selected stop: map trains
- [ ] Live updates on browser using ReactJS (or a similar platform)
- [ ] If no train is present on the scope of 2 stops, show minutes until next train (Same case for terminals)
- [x] Flat design

#### **Specifics and Other Information**

- Script will be written in Python, will get data from the MBTA V3 API
- Frontend will consist of simple HTML with elements of ReactJS for real time refreshing

#### **UI Brainstorm**

![alt text](https://i.ibb.co/DWD7twN/2019-08-08-11-39-33.png)
