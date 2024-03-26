package main

import (
	"context"
	"fmt"
	"os"
	"sync"
	"weather/service"

	"github.com/carlmjohnson/requests"
)

func Call15DaysWeatherApi(ctx context.Context, token string, location_id string, lang string, wg *sync.WaitGroup) {
	// location id: https://github.com/qwd/LocationList?tab=readme-ov-file
	defer wg.Done()
	var s string
	var err error
	req := requests.URL(fmt.Sprintf("https://devapi.qweather.com/v7/weather/15d?location=%s&key=%s&lang=%s", location_id, token, lang))
	err = req.ToString(&s).Fetch(ctx)
	if err != nil {
		fmt.Printf("Call15DaysWeatherApi failed: %s", err.Error())
		return
	}
	err = service.WriteData(s, "15d_data")
	if err != nil {
		fmt.Printf("write data failed: %s", err.Error())
		return
	}

}

func CallAqiApi(ctx context.Context, token string, location_id string, lang string, wg *sync.WaitGroup) {
	// location id: https://github.com/qwd/LocationList?tab=readme-ov-file
	defer wg.Done()
	var s string
	var err error
	req := requests.URL(fmt.Sprintf("https://devapi.qweather.com/v7/air/5d?location=%s&key=%s&lang=%s", location_id, token, lang))
	err = req.ToString(&s).Fetch(ctx)
	if err != nil {
		fmt.Printf("CallAqiApi failed: %s", err.Error())
		return
	}
	err = service.WriteData(s, "aqi_data")
	if err != nil {
		fmt.Printf("write data failed: %s", err.Error())
		return
	}

}

func main() {
	var wg sync.WaitGroup

	ctx := context.TODO()
	wg.Add(1)
	go Call15DaysWeatherApi(ctx, os.Args[1], os.Args[2], "en", &wg)
	wg.Add(1)
	go CallAqiApi(ctx, os.Args[1], os.Args[2], "en", &wg)

	wg.Wait()
}
