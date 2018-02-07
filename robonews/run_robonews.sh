#/bin/sh

echo "주식실시간크롤링을 시작합니다."

cd /root/scrapy/robonews
time=$(date '+%d-%H%M')
scrapy crawl index -o store/$(date '+%Y-%m')/index_$time.json
echo "주식실시간크롤링이 종료되었습니다."
echo "크롤링 데이터 수 : " 
grep ename store/$(date '+%Y-%m')/index_$time.json | wc -l

