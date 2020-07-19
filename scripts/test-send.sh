#!/bin/sh

export API_URL=https://icfpc2020-api.testkontur.ru
export API_KEY=6bf5652a02aa4dbfa34c03b800e57d13

curl -X POST "$API_URL/aliens/send?apiKey=$API_KEY" -H "accept: */*" -H "Content-Type: text/plain" -d "1010"
