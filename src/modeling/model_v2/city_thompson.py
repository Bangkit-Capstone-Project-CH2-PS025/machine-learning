class CityThompson():
    def init(self):
        self.keywords = []
        self.expected_keywords = []

    def select_city(self, city):
        if city == "bandung":
            return self.bandung()
        elif city == "banjarbaru":
            return self.banjarbaru()
        elif city == "bengkulu":
            return self.bengkulu()
        elif city == "denpasar":
            return self.denpasar()
        elif city == "jakarta":
            return self.jakarta()
        elif city == "jayapura":
            return self.jayapura()
        elif city == "maluku":
            return self.maluku()
        elif city == "semarang":
            return self.semarang()
        elif city == "surabaya":
            return self.surabaya()
        elif city == "yogyakarta":
            return self.yogyakarta()

    def bandung(self):
        self.keywords = ['taman', 'kota', 'alam', 'wisata', 'air', 'curug', 'museum', 'gunung', 'kawasan', 'rekreasi',
                         'batu', 'gedung', 'indah', 'jalan', 'hutan', 'tinggi', 'budaya', 'kolam', 'luas', 'seni']
        self.expected_keywords = ['museum', 'kota', 'gunung', 'taman', 'wisata']
        return self.keywords, self.expected_keywords

    def banjarbaru(self):
        self.keywords = ['wisata', 'rekreasi', 'taman', 'alam', 'air', 'danau', 'hutan', 'bukit', 'gunung', 'pinus',
                         'terjun', 'kebun', 'wisatawan', 'kalimantan', 'main', 'hijau', 'suasana', 'raya', 'pulau',
                         'kota']
        self.expected_keywords = ['taman', 'rekreasi', 'gunung', 'bukit', 'wisata']
        return self.keywords, self.expected_keywords

    def bengkulu(self):
        self.keywords = ['pantai', 'wisata', 'kota', 'alam', 'taman', 'indah', 'danau', 'pulau', 'air',
                         'pasar', 'jalan', 'wisatawan', 'wahana', 'pusat', 'luas', 'masyarakat', 'rekreasi', 'sejarah',
                         'laut', 'desa']
        self.expected_keywords = ['pantai', 'danau', 'wisata', 'alam', 'kota']
        return self.keywords, self.expected_keywords

    def denpasar(self):
        self.keywords = ['pantai', 'wisata', 'alam', 'kota', 'indah', 'wisatawan', 'pura', 'pulau', 'desa', 'pasir',
                         'selatan', 'taman', 'laut', 'budaya', 'warga', 'ombak', 'rekreasi', 'air', 'batu', 'selancar']
        self.expected_keywords = ['pantai', 'wisata', 'pura', 'kota', 'indah']
        return self.keywords, self.expected_keywords

    def jakarta(self):
        self.keywords = ['museum', 'taman', 'pulau', 'pusat', 'wisata', 'pantai', 'budaya', 'seni', 'sejarah',
                         'kawasan', 'pasar', 'kota', 'rekreasi', 'nasional', 'rumah', 'jalan', 'alam', 'masjid', 'luas',
                         'monumen']
        self.expected_keywords = ['museum', 'taman', 'pulau', 'pusat', 'budaya']
        return self.keywords, self.expected_keywords

    def jayapura(self):
        self.keywords = ['pantai', 'bukit', 'alam', 'kota', 'air', 'pasir', 'wisata', 'kampung', 'indah', 'pandang',
                         'telaga', 'teluk', 'distrik', 'laut', 'gunung', 'tanjung', 'destinasi', 'adat', 'danau',
                         'main']
        self.expected_keywords = ['pantai', 'bukit', 'air', 'kota', 'alam']
        return self.keywords, self.expected_keywords

    def maluku(self):
        self.keywords = ['pantai', 'pulau', 'alam', 'benteng', 'air', 'wisata', 'terjun', 'kota', 'indah', 'desa',
                         'laut', 'terjun', 'danau', 'sejarah', 'gunung', 'budaya', 'pasir', 'teluk', 'destinasi',
                         'tebing']
        self.expected_keywords = ['pantai', 'pulau', 'air', 'alam', 'benteng']
        return self.keywords, self.expected_keywords

    def semarang(self):
        self.keywords = ['wisata', 'taman', 'kota', 'pantai', 'alam', 'hutan', 'kampung', 'gunung', 'kawasan',
                         'rekreasi', 'air', 'sejarah', 'desa', 'jalan', 'masjid', 'batik', 'museum', 'pandang', 'rawa',
                         'budaya']
        self.expected_keywords = ['taman', 'wisata', 'kota', 'kampung', 'museum']
        return self.keywords, self.expected_keywords

    def surabaya(self):
        self.keywords = ['taman', 'kota', 'museum', 'wisata', 'patung', 'jalan', 'rekreasi', 'air', 'sejarah',
                         'monumen', 'masjid', 'laut', 'jembatan', 'waterpark', 'pantai', 'budaya', 'kebun', 'kapal',
                         'fasilitas', 'keluarga']
        self.expected_keywords = ['taman', 'museum', 'kota', 'masjid', 'monumen']
        return self.keywords, self.expected_keywords

    def yogyakarta(self):
        self.keywords = ['taman', 'kota', 'museum', 'wisata', 'patung', 'jalan', 'rekreasi', 'air', 'sejarah',
                         'monumen', 'masjid', 'laut', 'jembatan', 'waterpark', 'pantai', 'budaya', 'kebun', 'kapal',
                         'fasilitas', 'keluarga']
        self.expected_keywords = ['pantai', 'wisata', 'bukit', 'candi', 'gunung']
        return self.keywords, self.expected_keywords