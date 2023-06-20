{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "product_name": {
      "type": "string"
    },
    "product_status": {
      "type": "string"
    },
    "product_price": {
      "type": "number"
    },
    "effective_price_start_date": {
      "type": "string"
    },
    "effective_price_end_date": {
      "type": "string"
    },
    "quantity": {
      "type": "integer"
    },
    "product_details": {
      "type": "object",
      "properties": {
        "product_category": {
          "type": "string"
        },
        "supplier_details": {
          "type": "object",
          "properties": {
            "supplier": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "name"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "name"
                  ]
                }
              ]
            }
          },
          "required": [
            "supplier"
          ]
        }
      },
      "required": [
        "product_category",
        "supplier_details"
      ]
    },
    "created_date": {
      "type": "integer"
    },
    "updated_date": {
      "type": "string"
    },
    "updated_time": {
      "type": "integer"
    },
    "product_history": {
      "type": "object",
      "properties": {
        "product_price_history": {
          "type": "array",
          "items": [
            {
              "type": "object",
              "properties": {
                "price": {
                  "type": "number"
                },
                "start_date": {
                  "type": "string"
                },
                "end_date": {
                  "type": "string"
                }
              },
              "required": [
                "price",
                "start_date",
                "end_date"
              ]
            },
            {
              "type": "object",
              "properties": {
                "price": {
                  "type": "number"
                },
                "start_date": {
                  "type": "string"
                },
                "end_date": {
                  "type": "string"
                }
              },
              "required": [
                "price",
                "start_date",
                "end_date"
              ]
            }
          ]
        }
      },
      "required": [
        "product_price_history"
      ]
    }
  },
  "required": [
    "product_name",
    "product_status",
    "product_price",
    "effective_price_start_date",
    "effective_price_end_date",
    "quantity",
    "product_details",
    "created_date",
    "updated_date",
    "updated_time",
    "product_history"
  ]
}
