package model

type Aqi struct {
	FxDate   string `json:"fxDate"`
	Aqi      string `json:"aqi"`
	Level    string `json:"level"`
	Category string `json:"category"`
	Primary  string `json:"primary"`
}
