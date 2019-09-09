#!/bin/bash

# download historical data from yahoo finance

# example
# bash yahoo_finance_downloader.sh --ticker SPY --freq 1d --start_date 20171231 --end_date 20181231


function utc_to_unix() {
	date -u -d "$1 00:00:00 UTC" +%s
}

function unix_to_utc() {
	date -u -d @$1 '+%Y%m%d'
}

cookie_jar=$(mktemp)
function cleanup() {
	rm $cookie_jar
}
trap cleanup EXIT

function get_crumb() {
	crumb_url="https://ca.finance.yahoo.com/quote/$1/history?p=$1"
	curl -s --cookie-jar "$2" $crumb_url | sed 's+}+\n+g' | grep CrumbStore | cut -d ":" -f 3 | sed 's+"++g'
}


ticker="SP"
freq="1d" # "1wk
human_start_date=$(date -u --date="1 year ago" '+%Y%m%d')
human_end_date="" # $(date -u '+%Y%m%d')
while [ $# -ne 0 ]; do
	arg="$1"
	case "$arg" in
		--ticker) ticker="$2"; shift;;
		--freq) freq="$2"; shift;;
		--start_date) human_start_date="$2"; shift;;
		--end_date) human_end_date="$2"; shift;;
	esac
	shift
done


if [ -z "$human_end_date" ]; then
	human_end_date=`date -u -d "$human_start_date 00:00:00 UTC + 1 year" '+%Y%m%d'`
fi
start_date=`utc_to_unix $human_start_date`
end_date=`utc_to_unix $human_end_date`
crumb=`get_crumb $ticker $cookie_jar`
# echo $crumb $cookie_jar

request_url="https://query1.finance.yahoo.com/v7/finance/download/$ticker?period1=$start_date&period2=$end_date&interval=$freq&events=history&crumb=$crumb"
# echo "download $ticker data between" `unix_to_utc $start_date` `unix_to_utc $end_date` "from $request_url" #  "to $output_file"
curl -s --cookie $cookie_jar $request_url
