class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == 'Sulfuras, Hand of Ragnaros':
                item.quality = 80
                item.sell_in = item.sell_in - 1
                continue
            elif item.name == 'Aged Brie':
                self.fragant_method(item)
                continue

            elif 'Conjured' in item.name:
                item.quality -= 2
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality -= 2

            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                self.exclusive_method(item)
                continue

            else:
                self.common_item(item)

    def common_item(self, item):
        item.quality -= 1
        item.quality = max(item.quality, 0)
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality -= 1
            item.quality = max(item.quality, 0)

    def fragant_method(self, item):
        item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality += 1
        item.quality = min(item.quality, 50)

    def exclusive_method(self, item):
        if item.sell_in < 6:
            item.quality += 3
        elif item.sell_in < 11:
            item.quality += 2
        else:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        item.quality = min(item.quality, 50)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f'{self.name}, {self.sell_in}, {self.quality}'
