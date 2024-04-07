import time
def search_pattern_naive(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            occurrences.append(i)
    return occurrences

def search_pattern_boyer_moore_hash(text, pattern):
    def generate_bad_character_table(pattern):
        table = {}
        for i in range(len(pattern) - 1):
            table[pattern[i]] = len(pattern) - i - 1
        return table
    
    def hash_value(s):
        hash_sum = 0
        for char in s:
            hash_sum += ord(char)
        return hash_sum
    
    def boyer_moore_hash(text, pattern):
        n = len(text)
        m = len(pattern)
        table = generate_bad_character_table(pattern)
        pattern_hash = hash_value(pattern)
        occurrences = []
        i = 0
        while i <= n - m:
            if hash_value(text[i:i+m]) == pattern_hash:
                if text[i:i+m] == pattern:
                    occurrences.append(i)
                    i += m
                else:
                    i += 1
            else:
                i += max(1, table.get(text[i + m - 1], m))
        return occurrences
    
    return boyer_moore_hash(text, pattern)

text = """Czy backup danych jest potrzebny? Jak go wykonywać dobrze?
Ochrona danych to obecnie priorytet dla wielu firm - ponad 80% przedsiębiorstw twierdzi, że dba o bezpieczeństwo informacji w sieci. Jednak 75% z nich wciąż nie ma planu naprawczego na wypadek utraty danych. Co więcej, mniej niż połowa firm inwestuje wystarczająco dużo w zabezpieczenia. Aby je poprawić, warto regularnie wykonywać backup danych. Co to jest, jakie są jego rodzaje i jak skutecznie go przygotować? 
Co to jest backup?
Backup jest kopią zapasową danych, które przechowywane są na innych komputerach lub zewnętrznych serwerach. Ma za zadanie zwiększyć bezpieczeństwo i zminimalizować ryzyko całkowitej utraty plików na wypadek ataku hakerskiego, klęski żywiołowej (pożaru, powodzi), kradzieży lub awarii. Przykładowo, aż 2 na 3 firmy w USA doświadczyły problemów związanych z utratą informacji, które były spowodowane atakiem malware. Cyberprzestępstwa są więc powszechnym i realnym zagrożeniem.

Backup może dotyczyć danych przedsiębiorstwa, informacji o pracownikach, klientach i kontrahentach. Na serwerach przechowywane są pliki z wielu urządzeń znajdujących się w organizacji, dzięki czemu można uzyskać do nich dostęp w razie ataku czy awarii sprzętu. Dlatego warto przeprowadzać kopię zapasową jak najczęściej. Niestety, jedynie 10% przedsiębiorstw przeprowadza codzienny backup danych.
Dlaczego kopia zapasowa jest tak ważna?
Dane dotyczące pracowników, klientów i projektów firmy są kluczowe dla jej funkcjonowania. Ich utrata może doprowadzić do poważnych konsekwencji finansowych i wizerunkowych. 

Koszty związane z utratą danych
Przeciętny koszt cyberataku na dane firmy w Polsce wynosi ponad milion złotych! Najczęściej to koszty związane z okupem, działaniami prewencyjnymi oraz przywróceniem systemów i informacji po ataku. Backup może być przydatny na wypadek:
ataku hakerskiego;
klęski żywiołowej;
kradzieży;
błędów ludzkich;
uszkodzenia sprzętu;
awarii oprogramowania.
Takie zdarzenia mogą mieć miejsce w każdej firmie, dlatego warto posiadać kopię zapasową, dzięki której jesteś w stanie przywrócić utracone informacje.
Oszczędność czasu
Tworzenie backupu jest również oszczędnością czasu i nerwów. Przywrócenie kluczowych plików z kopii zapasowej jest znacznie szybsze niż próba odzyskania skradzionych lub skasowanych danych, które nie były poddane replikacji.

Regularne wykonywanie kopii zapasowej jest kluczowe dla prawidłowego funkcjonowania całej organizacji. Ponadto badania pokazują, że 60% firm, które nie decydują się na regularne wykonywanie kopii zapasowej i utraciły ważne informacje, upadają w ciągu 6 miesięcy. W takiej sytuacji backup danych może być zbawienny, ponieważ błyskawicznie jesteś w stanie odzyskać utracone informacje w krótkim czasie.

Backup danych - rodzaje
Wyróżniamy trzy główne rodzaje backupów, które różnią się od siebie sposobem zapisywania i przechowywania danych.
Backup pełny
To kompletna kopia zapasowa danych. Tworzy idealnie odwzorowany obraz systemów sprzed wystąpienia awarii. Jest to najbezpieczniejsze rozwiązanie, które daje dostęp do 100% danych. Jednak konieczne jest dysponowanie sporą powierzchnią dyskową oraz cierpliwością, ponieważ rozwiązanie to jest czasochłonne.
Backup kumulacyjny
To forma kopii zapasowej, która replikuje tylko i wyłącznie te dane, które zostały dodane lub zmodyfikowane od ostatniego pełnego backupu. W ten sposób można zaoszczędzić czas i przestrzeń dyskową, ale do odtworzenia pełnego obrazu systemu konieczne jest skorzystanie z ostatniego pełnego i najnowszego kumulacyjnego backupu.
Backup przyrostowy
To rozwiązanie najszybsze i zajmujące najmniej miejsca. Wiąże się to jednak z faktem, że jest to najmniej kompletna kopia zapasowa. Kopiowane są tylko te pliki, które zostały zmodyfikowane od ostatniego przyrostowego backupu. Niestety w przypadku awarii i konieczności przywrócenia pełnej kopii, niezbędne będzie odtworzenie ostatniej pełnej kopii i wszystkich pomniejszych.

Ponadto możemy podzielić backup danych ze względu na miejsce występowania. Warto zapoznać się z zaletami i wadami obu rozwiązań.
Sprzętowy backup danych
Zalety:
niskie koszty związane z utrzymaniem infrastruktury;
możliwość szybkiego przywrócenia informacji;
łatwa kontrola nad danymi.
Wady:
wyższe ryzyko wystąpienia awarii;
możliwość mechanicznego uszkodzenia;
skalowalność przestrzeni dyskowej wiąże się z inwestycją w kolejne dyski.
Backup danych w chmurze
Zalety:
łatwa i praktycznie nieograniczona skalowalność przestrzeni serwerowej;
wysoki poziom bezpieczeństwa danych;
dostęp do danych z dowolnego miejsca na świecie.

Wady:
wolniejsze przywrócenie informacji;
konieczność posiadania dostępu do Internetu.

Jeśli potrzebujesz rozwiązania, które jest praktycznie nieograniczone i planujesz skalować swój biznes, lepszym  rozwiązaniem będzie backup w chmurze. Podobnie w sytuacji, gdy twoja firma w dużym stopniu funkcjonuje zdalnie, ponieważ dostęp do informacji można uzyskać z dowolnego miejsca. Natomiast w sytuacji, gdy szukasz oszczędności i prostej obsługi, powinieneś zdecydować się na sprzętowy backup danych.
Jak poprawnie wykonać kopię zapasową?
W przypadku kopii zapasowej kluczowe jest jej odpowiednie wykonanie. Podręcznikowy model zakłada korzystanie z reguły 3-2-1, czyli powinieneś stworzyć co najmniej 3 kopie plików, które powinny być przechowywane na minimum 2 różnych urządzeniach, a jedno z nich powinno znajdować się w innym miejscu niż siedziba firmy. Dodatkowo można zwiększyć bezpieczeństwo, jeśli jedną z kopii będziesz przechowywać na urządzeniu offline.

W przypadku przeprowadzania kopii zapasowej należy pamiętać o kilku zasadach:
przeprowadzaj backup możliwie jak najczęściej;
korzystaj z kilku rodzajów nośników;
przeprowadzaj automatyczne tworzenie kopii zapasowej;
replikuj dane z wszystkich urządzeń, na których znajdują się ważne dla firmy pliki;
regularnie przeprowadzaj aktualizacje oprogramowania.


Backup-as-a-Service - co to jest?
Kluczowym aspektem w kontekście bezpieczeństwa danych jest skuteczny backup. Dlatego warto postawić na wiedzę i umiejętności specjalistów. W Cloud4You oferujemy usługę Backup-as-a-Service, która przeznaczona jest do replikacji kopii zapasowych. Rozwiązanie to jest dedykowane organizacjom, które potrzebują niezawodnego sposobu na zabezpieczenie informacji przed ich utratą. Ponadto w krótkim czasie można przywrócić zapisane dane. W ramach usługi BaaS możesz liczyć na:

administrowanie systemem backupu oraz zarządzanie kopią zapasową;
odzyskiwanie danych na zlecenie;
monitorowanie systemów backupu;
weryfikację poprawności wykonanych kopii zapasowych.
Podsumowanie
Regularne przeprowadzanie kopii zapasowej jest kluczowym aspektem w kontekście prowadzenia biznesu w 2023 roku. Informacje są dziś bezcenne, dlatego warto przygotować się na ewentualne awarie i profilaktycznie wykonywać backup danych. W ten sposób można zaoszczędzić mnóstwo pieniędzy. Nie zwlekaj i zadbaj o swoje cenne informacje już dziś, kontaktując się z naszymi specjalistami.

"""
pattern = "backup"

start_time_naive = time.time()
occurrences_naive = search_pattern_naive(text, pattern)
end_time_naive = time.time()
time_naive = end_time_naive - start_time_naive

start_time_bm_hash = time.time()
occurrences_bm_hash = search_pattern_boyer_moore_hash(text, pattern)
end_time_bm_hash = time.time()
time_bm_hash = end_time_bm_hash - start_time_bm_hash

print("Algorytm naiwny:")
print("Liczba wystąpień wzorca:", len(occurrences_naive))
print("Czas wykonania:", time_naive)


print("Algorytm Boyera-Moore'a z wykorzystaniem hashowania:")
print("Liczba wystąpień wzorca:", len(occurrences_bm_hash))
print("Czas wykonania:", time_bm_hash)

