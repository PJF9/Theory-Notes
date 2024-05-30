#ifdef STRING


namespace pjf {
    
    string::string() {}





    string::string(const char &letter) {
        this->s.array_size = 1;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        delete[] this->s.arr;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        this->s.arr[0] = letter;
    }





    string::string(const char *cstring) {
        this->s.array_size = this->__get_cstring_size(cstring);
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        delete[] this->s.arr;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = cstring[i];
        }
    }





    string::string(const string &str) {
        this->s.array_size = str.s.length();
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        delete[] this->s.arr;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = str.s.get(i);
        }
    }





    string::string(const std::string &str) {
        this->s.array_size = str.size();
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        delete[] this->s.arr;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = str[i];
        }
    }





    string::string(const array<int> &ascii_arr) {
        this->s.array_size = ascii_arr.length();
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        delete[] this->s.arr;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->length(); ++i) {
            this->s.arr[i] = (char) ascii_arr[i];
        }
    }





    string::~string() {}





    char string::get(int index) const {
        if (index > this->length() || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        return this->s.get(index);
    }





    string::iterator string::get_iter(int index) const {
        if (index > this->length() - 1 || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        return string::iterator(this->begin() + index);
    }





    string::const_iterator string::get_citer(int index) const {
        if (index > this->length() - 1 || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        return string::const_iterator(this->cbegin() + index);
    }





    void string::set_length(int new_size, const char &elem) {
        if (new_size < 0) {
            std::cout << "Cannot compress the string to negative size." << std::endl;
            this->s.~array();
            throw -7;
        }

        this->s.set_length(new_size, elem);
    }





    void string::set_size(int new_extended_size) {
        if (new_extended_size < this->length()) {
            std::cout << "New memory size must be highter than the length of the string." << std::endl;
            this->s.~array();
            throw -7;
        }

        this->s.set_size(new_extended_size);
    }





    string string::push_back(const char &letter) {
        this->s.push_back(letter);

        return *this;
    }





    string string::push_front(const char &letter) {
        this->s.push_front(letter);

        return *this;
    }





    string string::insert(int index, const char &letter) {
        if (index > this->length() || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        this->s.insert(index, letter);

        return *this;
    }





    string string::insert(string::iterator &position, const char &new_letter) {
        int index = this->__get_iter_index(*this, position);

        if (index == this->length()+1) {
            std::cout << "The iterator that have been passed is either not created by the 'this' string or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        this->insert(index, new_letter);
    }





    string string::insert(string::const_iterator &position, const char &new_letter) {
        const int index = this->__get_iter_index(*this, position);

        if (index == this->length()+1) {
            std::cout << "The iterator that have been passed is either not created by the 'this' string or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        this->insert(index, new_letter);
    }





    string string::extend(const char *cstring) {
        int csize = this->__get_cstring_size(cstring);

        char *temp = new(std::nothrow) char [this->length() + csize];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->length(); ++i) {
            temp[i] = this->s.arr[i];
        }
        for (int i=0; i<csize; ++i) {
            temp[this->length() + i] = cstring[i];
        }

        delete[] this->s.arr;

        this->s.array_size = this->length() + csize;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::extend(const std::string &str) {
        char *temp = new(std::nothrow) char [this->length() + str.length()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->length(); ++i) {
            temp[i] = this->s.arr[i];
        }
        for (int i=0; i<str.length(); ++i) {
            temp[this->length() + i] = str[i];
        }

        delete[] this->s.arr;

        this->s.array_size = this->length() + str.length();
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::extend(const string &str) {
        char *temp = new(std::nothrow) char [this->length() + str.length()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->length(); ++i) {
            temp[i] = this->s.arr[i];
        }
        for (int i=0; i<str.length(); ++i) {
            temp[this->length() + i] = str[i];
        }

        delete[] this->s.arr;

        this->s.array_size = this->length() + str.length();
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::extend(const char *cstring, int index) {
        if (index > this->length() || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        int csize = this->__get_cstring_size(cstring);

        char *temp = new(std::nothrow) char [this->length() + csize];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int i = 0;
        while (i < index) {
            temp[i] = this->s.arr[i];
            ++i;
        }
        int k = i;
        for (int j=0; j<csize; ++j) {
            temp[i++] = cstring[j];
        }
        while (i < this->length() + csize) {
            temp[i++] = this->s.arr[k++];
        }

        delete[] this->s.arr;

        this->s.array_size = i;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::extend(const std::string &str, int index) {
        if (index > this->length() || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        char *temp = new(std::nothrow) char [this->length() + str.length()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int i = 0;
        while (i < index) {
            temp[i] = this->s.arr[i];
            ++i;
        }
        int k = i;
        for (int j=0; j<str.length(); ++j) {
            temp[i++] = str[j];
        }
        while (i < this->length() + str.length()) {
            temp[i++] = this->s.arr[k++];
        }

        delete[] this->s.arr;

        this->s.array_size = i;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::extend(const string &str, int index) {
        if (index > this->length() || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        char *temp = new(std::nothrow) char [this->length() + str.length()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int i = 0;
        while (i < index) {
            temp[i] = this->s.arr[i];
            ++i;
        }
        int k = i;
        for (int j=0; j<str.length(); ++j) {
            temp[i++] = str[j];
        }
        while (i < this->length() + str.length()) {
            temp[i++] = this->s.arr[k++];
        }

        delete[] this->s.arr;

        this->s.array_size = i;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::extend(string::iterator &start, string::iterator &end, string &iters_object) {
        const int start_i = this->__get_iter_index(iters_object, start);
        const int end_i = this->__get_iter_index(iters_object, end);

        if (start_i == iters_object.length() + 1 || end_i == iters_object.length() + 1) {
            std::cout << "Invalid Iterator Positions: Iterators are out ouf bounds or have not been created by 'iters_object'." << std::endl;
            this->s.~array();
            throw -3;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        for (string::iterator it=start; it!=end; ++it) {
            this->push_back(*it);
        }

        return *this;
    }





    string string::extend(string::const_iterator &start, string::const_iterator &end, string &iters_object) {
        const int start_i = this->__get_iter_index(iters_object, start);
        const int end_i = this->__get_iter_index(iters_object, end);

        if (start_i == iters_object.length() + 1 || end_i == iters_object.length() + 1) {
            std::cout << "Invalid Iterator Positions: Iterators are out ouf bounds or have not been created by 'iters_object'." << std::endl;
            this->s.~array();
            throw -3;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        for (string::const_iterator it=start; it!=end; ++it) {
            this->push_back(*it);
        }

        return *this;
    }





    string string::extend(std::string::iterator &start, std::string::iterator &end, std::string &iters_object) {
        const int start_i = this->__get_iter_index(iters_object, start);
        const int end_i = this->__get_iter_index(iters_object, end);

        if (start_i == iters_object.length() + 1 || end_i == iters_object.length() + 1) {
            std::cout << "Invalid Iterator Positions: Iterators are out ouf bounds or have not been created by 'iters_object'." << std::endl;
            this->s.~array();
            throw -3;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        for (std::string::iterator it=start; it!=end; ++it) {
            this->push_back(*it);
        }

        return *this;
    }





    string string::extend(std::string::const_iterator &start, std::string::const_iterator &end, std::string &iters_object) {
        const int start_i = this->__get_iter_index(iters_object, start);
        const int end_i = this->__get_iter_index(iters_object, end);

        if (start_i == iters_object.length() + 1 || end_i == iters_object.length() + 1) {
            std::cout << "Invalid Iterator Positions: Iterators are out ouf bounds or have not been created by 'iters_object'." << std::endl;
            this->s.~array();
            throw -3;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        for (std::string::const_iterator it=start; it!=end; ++it) {
            this->push_back(*it);
        }

        return *this;
    }






    string string::replace(int index, const char &letter) {
        if (index > (this->length()) || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        this->s[index] = letter;

        return *this;
    }





    string string::replace(int index, const char *cstring) {
        if (index > (this->length()) || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        int csize = this->__get_cstring_size(cstring);

        if (index + csize > this->size()) {
            char *temp = new(std::nothrow) char [index + csize];
            if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

            for (int i=0; i<index; ++i) {
                temp[i] = this->s.arr[i];
            }
            for (int i=index; i<csize + index; ++i) {
                temp[i] = cstring[i - index];
            }

            delete[] this->s.arr;

            this->s.array_size = index + csize;
            this->s.extended_size = this->s.array_size + ARRAY_GAP;

            this->s.arr = new(std::nothrow) char [this->s.extended_size];
            if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

            for (int i=0; i<this->s.array_size; ++i) {
                this->s.arr[i] = temp[i];
            }

            delete[] temp;
        }
        else {
            if (index + csize > this->s.array_size) {
                this->s.array_size = index + csize;
            }

            for (int i=0; i<csize; ++i) {
                this->s.arr[index + i] = cstring[i];
            }
        }

        return *this; 
    }





    string string::replace(int index, const std::string &str) {
        if (index > (this->length()) || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        if (index + str.length() > this->size()) {
            char *temp = new(std::nothrow) char [index + str.length()];
            if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

            for (int i=0; i<index; ++i) {
                temp[i] = this->s.arr[i];
            }
            for (int i=index; i<str.length() + index; ++i) {
                temp[i] = str[i - index];
            }

            delete[] this->s.arr;

            this->s.array_size = index + str.length();
            this->s.extended_size = this->s.array_size + ARRAY_GAP;

            this->s.arr = new(std::nothrow) char [this->s.extended_size];
            if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

            for (int i=0; i<this->s.array_size; ++i) {
                this->s.arr[i] = temp[i];
            }

            delete[] temp;
        }
        else {
            if (index + str.length() > this->s.array_size) {
                this->s.array_size = index + str.length();
            }

            for (int i=0; i<str.length(); ++i) {
                this->s.arr[index + i] = str[i];
            }
        }

        return *this;  
    }





    string string::replace(int index, const string &str) {
        if (index > (this->length()) || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        if (index + str.length() > this->size() || this == &str) {
            char *temp = new(std::nothrow) char [index + str.length()];
            if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

            for (int i=0; i<index; ++i) {
                temp[i] = this->s.arr[i];
            }
            for (int i=index; i<str.length() + index; ++i) {
                temp[i] = str[i - index];
            }

            delete[] this->s.arr;

            this->s.array_size = index + str.length();
            this->s.extended_size = this->s.array_size + ARRAY_GAP;

            this->s.arr = new(std::nothrow) char [this->s.extended_size];
            if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

            for (int i=0; i<this->s.array_size; ++i) {
                this->s.arr[i] = temp[i];
            }

            delete[] temp;
        }
        else {
            if (index + str.length() > this->s.array_size) {
                this->s.array_size = index + str.length();
            }

            for (int i=0; i<str.length(); ++i) {
                this->s.arr[index + i] = str[i];
            }
        }

        return *this;  
    }





    string string::replace(int index, int total_pos, const char &letter) {
        if (index + total_pos > this->length() || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        for (int i=index; i<index + total_pos + 1; ++i) {
            this->s[i] = letter;
        }

        return *this;
    }

    
    
    
    string string::replace(const char &letter1, const char &letter2) {
        for (int i=0; i<this->length(); ++i) {
            if (this->s.arr[i] == letter1) {
                this->s.arr[i] = letter2;
            }
        }

        return *this;
    }





    string string::replace(typename string::iterator &it, const char &new_letter) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has been passed is either not created by the 'this' object or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->replace(index, new_letter);

        return *this;
    }





    string string::replace(typename string::iterator &it, const char *cstring) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has been passed is either not created by the 'this' object or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->replace(index, cstring);

        return *this;
    }





    string string::replace(typename string::iterator &it, const std::string &str) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has been passed is either not created by the 'this' object or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->replace(index, str);

        return *this;
    }





    string string::replace(typename string::iterator &it, const string &str) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has been passed is either not created by the 'this' object or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->replace(index, str);

        return *this;
    }





    string string::replace(typename string::const_iterator &it, const char &new_letter) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has been passed is either not created by the 'this' object or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->replace(index, new_letter);

        return *this;
    }





    string string::replace(typename string::const_iterator &it, const char *cstring) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has been passed is either not created by the 'this' object or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->replace(index, cstring);

        return *this;
    }





    string string::replace(typename string::const_iterator &it, const std::string &str) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has been passed is either not created by the 'this' object or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->replace(index, str);

        return *this;
    }





    string string::replace(typename string::const_iterator &it, const string &str) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has been passed is either not created by the 'this' object or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->replace(index, str);

        return *this;
    }





    string string::replace(typename string::iterator &it, int total_pos, const char &letter) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has been passed is either not created be th 'this' string or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->replace(index, total_pos, letter);

        return *this;
    }





    string string::replace(typename string::const_iterator &it, int total_pos, const char &letter) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has been passed is either not created be th 'this' string or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->replace(index, total_pos, letter);

        return *this;
    }





    string string::pop_back() {
        this->s.pop_back();

        return *this;
    }





    string string::pop_front() {
        this->s.pop_front();

        return *this;
    }





    string string::clear() {
        this->s.clear();

        return *this;
    }





    string string::pop(int index, int total_pos) {
        this->s.pop(index, total_pos);

        return *this;
    }





    string string::pop(typename string::iterator &it) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has beem passed is either not created by the 'this' string or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->pop(index);

        return *this;
    }





    string string::pop(typename string::const_iterator &it) {
        if (!this->__iter_link_to_string(*this, it)) {
            std::cout << "The iterator that has beem passed is either not created by the 'this' string or is out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int index = this->at(it);

        this->pop(index);

        return *this;
    }





    string string::pop(typename string::iterator &start, typename string::iterator &end) {
        if (!this->__iter_link_to_string(*this, start) || !this->__iter_link_to_string(*this, end)) {
            std::cout << "The iterators that have been passed are either not been craeted by the 'this' string or are out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int start_i = this->at(start);
        int end_i = this->at(end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        this->pop(start_i, (end_i - start_i - 1));

        return *this;
    }





    string string::pop(typename string::const_iterator &start, typename string::const_iterator &end) {
        if (!this->__iter_link_to_string(*this, start) || !this->__iter_link_to_string(*this, end)) {
            std::cout << "The iterators that have been passed are either not been craeted by the 'this' string or are out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }

        int start_i = this->at(start);
        int end_i = this->at(end);

        if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        this->pop(start_i, (end_i - start_i - 1));

        return *this;
    }





    string string::remove(const char &letter, bool dupl) {
        this->s.remove(letter, dupl);

        return *this;
    }





    string string::remove(const char *cstring, bool dupl) {
        char *temp = new(std::nothrow) char [this->length()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int csize = this->__get_cstring_size(cstring);
        int k = 0;
        bool found;
        bool first = false;
        for (int i=0; i<this->length(); ++i) {
            found = true;
            if (this->s.arr[i] == cstring[0] && i + csize <= this->length()) {
                for (int j=1; j<csize; ++j) {
                    if (this->s.arr[i+j] != cstring[j]) {
                        found = false;
                        break;
                    }
                }
                if (dupl) {
                    if (found) {
                        i += (csize - 1);
                        continue;
                    }
                }
                else {
                    if (found && !first) {
                        first = true;
                        i += (csize - 1);
                        continue;
                    }
                }
            }
            temp[k++] = this->s.arr[i];
        }

        delete[] this->s.arr;

        this->s.array_size = k;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (this->s.arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::remove(const std::string &str, bool dupl) {
        char *temp = new(std::nothrow) char [this->length()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int k = 0;
        bool found;
        bool first = false;
        for (int i=0; i<this->length(); ++i) {
            found = true;
            if (this->s.arr[i] == str[0] && i + str.length() <= this->length()) {
                for (int j=1; j<str.length(); ++j) {
                    if (this->s.arr[i+j] != str[j]) {
                        found = false;
                        break;
                    }
                }
                if (dupl) {
                    if (found) {
                        i += (str.length() - 1);
                        continue;
                    }
                }
                else {
                    if (found && !first) {
                        first = true;
                        i += (str.length() - 1);
                        continue;
                    }
                }
            }
            temp[k++] = this->s.arr[i];
        }

        delete[] this->s.arr;

        this->s.array_size = k;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (this->s.arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::remove(const string &str, bool dupl) {
        char *temp = new(std::nothrow) char [this->length()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int k = 0;
        bool found;
        bool first = false;
        for (int i=0; i<this->length(); ++i) {
            found = true;
            if (this->s.arr[i] == str[0] && i + str.length() <= this->length()) {
                for (int j=1; j<str.length(); ++j) {
                    if (this->s.arr[i+j] != str[j]) {
                        found = false;
                        break;
                    }
                }
                if (dupl) {
                    if (found) {
                        i += (str.length() - 1);
                        continue;
                    }
                }
                else {
                    if (found && !first) {
                        first = true;
                        i += (str.length() - 1);
                        continue;
                    }
                }
            }
            temp[k++] = this->s.arr[i];
        }

        delete[] this->s.arr;

        this->s.array_size = k;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (this->s.arr == nullptr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::delete_dupls() {
        this->s.delete_dupls();

        return *this;
    }





    string string::rev_string() {
        this->s.rev_array();

        return *this;
    }





    string string::rev_string(typename string::iterator &start, typename string::iterator &end) {
        int start_i = this->__get_iter_index(*this, start);
        int end_i = this->__get_iter_index(*this, end);

        if (start_i == this->length()+1 || end_i == this->length()+1) {
            std::cout << "The iterators that have been passed are either not been craeted by the 'this' string or are out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        string temp = this->slice(start_i, end_i);
        temp.rev_string();

        for (int i=0; i<temp.length(); ++i) {
            this->s.arr[start_i+i] = temp[i];
        }

        return *this;
    }





    string string::rev_string(typename string::const_iterator &start, typename string::const_iterator &end) {
        int start_i = this->__get_iter_index(*this, start);
        int end_i = this->__get_iter_index(*this, end);

        if (start_i == this->length()+1 || end_i == this->length()+1) {
            std::cout << "The iterators that have been passed are either not been craeted by the 'this' string or are out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        string temp = this->slice(start_i, end_i);
        temp.rev_string();

        for (int i=0; i<temp.length(); ++i) {
            this->s.arr[start_i+i] = temp[i];
        }

        return *this;
    }





    string string::shuffle() {
        this->s.shuffle();

        return *this;
    }





    string string::adjust_left(int new_length, const char &filler) {
        if (new_length < this->length()) {
            std::cout << "New length must be highter than the prior one." << std::endl;
            this->s.~array();
            throw -8;
        }

        char *temp = new(std::nothrow) char [new_length];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->length(); ++i) {
            temp[i] = this->s.arr[i];
        }
        for (int i=this->length(); i<new_length; ++i) {
            temp[i] = filler;
        }

        delete[] this->s.arr;

        this->s.array_size = new_length;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }
        
        delete[] temp;

        return *this;
    }





    string string::adjust_right(const int new_length, const char &filler) {
        if (new_length < this->length()) {
            std::cout << "New length must be highter than the prior one." << std::endl;
            this->s.~array();
            throw -8;
        }

        char *temp = new(std::nothrow) char [new_length];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<(new_length-this->length()); ++i) {
            temp[i] = filler;
        }
        for (int i=(new_length-this->length()); i<new_length; ++i) {
            temp[i] = this->s.arr[i - (new_length-this->length())];
        }

        delete[] this->s.arr;

        this->s.array_size = new_length;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }
        
        delete[] temp;

        return *this;
    }





    template <typename _Type>
    string string::format(const std::initializer_list<_Type> &il) {
        array<int> indexes_arr = this->indexes("{}");

        int list_size = 0;
        const _Type *p = il.begin();

        while (p != il.end()) {
            p = il.begin() + list_size;
            list_size ++;
        }
        list_size --;
        

        if (indexes_arr.length() > list_size) {
            std::cout << "The arguments that have beed passed are less than expected." << std::endl;
            std::cout << "Expected: " << indexes_arr.length() << ", but got: " << list_size << std::endl;
            this->s.~array();
            throw -9;
        }
        else if (indexes_arr.length() < list_size) {
            std::cout << "The arguments that have been passed are more than expected." << std::endl;
            std::cout << "Expected: " << indexes_arr.length() << ", but got: " << list_size << std::endl;
            this->s.~array();
            throw -9;
        }

        array<string> arr = this->split("{");
        this->clear();

        int j = 0;
        for (int i=0; i<arr.length(); i++) {
            if (arr[i].startswith('}')) {
                arr[i].pop(0);
                arr[i].extend(make_string(*(il.begin() + j)), 0);
                j ++;
            }
            this->extend(arr[i]);
        }

        return *this;
    }





    string string::copy(const char &letter) {
        delete[] this->s.arr;

        this->s.array_size = 1;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        this->s.arr[0] = letter;

        return *this;
    }





    string string::copy(const char *cstring) {
        int csize = this->__get_cstring_size(cstring);

        char *temp = new(std::nothrow) char[csize];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<csize; ++i) {
            temp[i] = cstring[i];
        }

        delete[] this->s.arr;

        this->s.array_size = csize;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::copy(const char *cstring, int start_i, int end_i) {
        if (start_i < 0 || end_i < 0 || end_i > this->__get_cstring_size(cstring) || start_i > end_i) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        int csize = this->__get_cstring_size(cstring);

        char *temp = new(std::nothrow) char[csize];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int j = 0;
        for (int i=start_i; i<end_i; i++) {
            temp[j++] = cstring[i];
        }

        delete[] this->s.arr;

        this->s.array_size = j;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::copy(const std::string &str) {
        char *temp = new(std::nothrow) char[str.size()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); exit(0);}

        for (int i=0; i<str.size(); i++) {
            temp[i] = str[i];
        }

        delete[] this->s.arr;

        this->s.array_size = str.size();
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this; 
    }





    string string::copy(const std::string &str, int start_i, int end_i) {
        if (start_i < 0 || end_i < 0 || end_i > str.size() || start_i > end_i) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        char *temp = new(std::nothrow) char[str.size()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int j = 0;
        for (int i=start_i; i<end_i; i++) {
            temp[j++] = str[i];
        }

        delete[] this->s.arr;

        this->s.array_size = j;
        this->s.extended_size = this->length() + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;   
    }





    string string::copy(const string &str) {
        this->s.copy(str.s);

        return *this;
    }





    string string::copy(const string &str, int start_i, int end_i) {
        if (start_i < 0 || end_i < 0 || end_i > str.length() || start_i > end_i) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        this->s.copy(str.s, start_i, end_i);

        return *this;
    }





    string string::copy(typename string::iterator &start, typename string::iterator &end, string &iters_object) {
        int start_i = this->__get_iter_index(iters_object, start);
        int end_i = this->__get_iter_index(iters_object, end);

        if (start_i == iters_object.length() + 1 || end_i == iters_object.length() + 1) {
            std::cout << "The iterators that beve been passed are either not created by the 'iters_object' string or out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        this->copy(iters_object.slice(start_i, end_i));

        return *this;
    }





    string string::copy(typename string::const_iterator &start, typename string::const_iterator &end, string &iters_object) {
        int start_i = this->__get_iter_index(iters_object, start);
        int end_i = this->__get_iter_index(iters_object, end);

        if (start_i == iters_object.length() + 1 || end_i == iters_object.length() + 1) {
            std::cout << "The iterators that beve been passed are either not created by the 'iters_object' string or out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        this->copy(iters_object.slice(start_i, end_i));

        return *this;
    }





    string string::copy(typename std::string::iterator &start, typename std::string::iterator &end, std::string &iters_object) {
        int start_i = this->__get_iter_index(iters_object, start);
        int end_i = this->__get_iter_index(iters_object, end);

        if (start_i == iters_object.size() + 1 || end_i == iters_object.size() + 1) {
            std::cout << "The iterators that beve been passed are either not created by the 'iters_object' string or out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        char *temp = new(std::nothrow) char[iters_object.size()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int j = 0;
        for (int i=start_i; i<end_i; i++) {
            temp[j++] = iters_object[i];
        }

        delete[] this->s.arr;

        this->s.array_size = j;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }
        delete[] temp;

        return *this;
    }





    string string::copy(typename std::string::const_iterator &start, typename std::string::const_iterator &end, const std::string &iters_object) {
        int start_i = this->__get_iter_index(iters_object, start);
        int end_i = this->__get_iter_index(iters_object, end);

        if (start_i == iters_object.size() + 1 || end_i == iters_object.size() + 1) {
            std::cout << "The iterators that beve been passed are either not created by the 'iters_object' string or out of bounds." << std::endl;
            this->s.~array();
            throw -3;
        }
        else if (start_i > end_i) {
            std::cout << "Invalid Iterator Positions." << std::endl;
            this->s.~array();
            throw -2;
        }

        char *temp = new(std::nothrow) char[iters_object.size()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int j = 0;
        for (int i=start_i; i<end_i; i++) {
            temp[j++] = iters_object[i];
        }

        delete[] this->s.arr;

        this->s.array_size = j;
        this->s.extended_size = this->length() + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->length(); ++i) {
            this->s.arr[i] = temp[i];
        }
        delete[] temp;

        return *this;
    }





    std::string string::to_std_string() const {
        std::string temp;
        for (int i=0; i<this->length(); ++i) {
            temp += this->s.arr[i];
        }

        return temp;
    }





    const char* string::to_cstring() const {
        char* temp = new(std::nothrow) char[this->length()];
        if (!temp) {std::cout << "Error Allocating Memory." << std::endl; this->s.~array(); exit(0);}

        for (int i=0; i<this->length(); i++) {
            temp[i] = this->s.arr[i];
        }
        temp[this->length()] = '\0';

        return temp;
    }





    array<char> string::to_array() const {
        return this->s;
    }





    array<int> string::give_ascii() const {
        array<int> arr;

        for (int i=0; i<this->length(); i++) {
            arr.push_back((int) this->s.arr[i]);
        }

        return arr;
    }





    string string::to_upper() {
        for (int i=0; i<this->length(); ++i) {
            if ((int) this->get(i) >= 97 && (int) this->get(i) <= 122) {
                (*this)[i] = (char)((*this)[i] - 32);
            }
        }

        return *this;
    }





    string string::to_upper(int start_i, int end_i) {
        if (start_i < 0 || end_i > this->length() || start_i > end_i) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        for (int i=start_i; i<end_i; ++i) {
            if ((int) this->get(i) >= 97 && (int) this->get(i) <= 122) {
                (*this)[i] = (char)((*this)[i] - 32);
            }
        }

        return *this;
    }





    string string::to_lower() {
        for (int i=0; i<this->length(); ++i) {
            if ((int) this->get(i) >= 65 && (int) this->get(i) <= 90) {
                (*this)[i] = (char)((*this)[i] + 32);
            }
        }

        return *this;
    }





    string string::to_lower(int start_i, int end_i) {
        if (start_i < 0 || end_i > this->length() || start_i > end_i) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        for (int i=start_i; i<end_i; ++i) {
            if ((int) this->get(i) >= 65 && (int) this->get(i) <= 90) {
                (*this)[i] = (char)((*this)[i] + 32);
            }
        }

        return *this;
    }





    string string::swap_case() {
        for (int i=0; i<this->length(); ++i) {
            if ((int) this->get(i) >= 65 && (int) this->get(i) <= 90) {
                (*this)[i] = (char)((*this)[i] + 32);
            }
            else if ((int) this->get(i) >= 97 && (int) this->get(i) <= 122) {
                (*this)[i] = (char)((*this)[i] - 32);
            }
        }

        return *this;
    }





    string string::swap_case(int start_i, int end_i) {
        if (start_i < 0 || end_i > this->length() || start_i > end_i) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        for (int i=start_i; i<end_i; ++i) {
            if ((int) this->get(i) >= 65 && (int) this->get(i) <= 90) {
                (*this)[i] = (char)((*this)[i] + 32);
            }
            else if ((int) this->get(i) >= 97 && (int) this->get(i) <= 122) {
                (*this)[i] = (char)((*this)[i] - 32);
            }
        }

        return *this;
    }





    int string::to_int() const {
        int num = 0;

        for (int i=0; i<this->length(); ++i) {
            int temp = 1;
            for (int j=0; j<this->length()-1-i; j++) {
                temp *= 10;
            }
            num += this->__char_to_int(this->s.arr[i]) * temp;
        }

        return num;
    }





    string string::capitalize() {
        if (this->length() != 0 && (this->s.arr[0] >= 97 && this->s.arr[0] <= 122)) {
            (*this)[0] = (char)((*this)[0] - 32);
        }

        return *this;
    }





    string string::title() {
        this->to_lower();
        if (this->length() != 0 && (this->s.arr[0] >= 97 && this->s.arr[0] <= 122)) {
            (*this)[0] = (char)((*this)[0] - 32);
        }

        return *this;
    }





    string string::swap(int first_i, int second_i) {
        if (first_i < 0 || second_i < 0 || second_i > this->length()-1 || first_i > this->length()-1) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        this->s.swap(first_i, second_i);

        return *this;
    }





    string string::swap(string &str) {
        string temp = *this;
        *this = str;
        str = temp;

        return *this;
    }





    string string::swap(std::string &str) {
        string temp = *this;
        *this = str;

        str.clear();
        
        for (int i=0; i<temp.length(); ++i) {
            str.push_back(temp[i]);
        }

        return *this;
    }





    string string::slice(int start, int end, int step) const {
        string temp;
        temp.s = this->s.slice(start, end, step);

        return temp;
    }





    string string::center(int new_length, const char &filler) {
        if (new_length < this->length()) {
            std::cout << "New length must be highter than the current one." << std::endl;
            this->s.~array();
            throw -2;
        }

        int difference = new_length - this->length();

        for (int i=0; i<difference/2; i++) {
            this->push_back(filler);
            this->push_front(filler);
        }

        return *this;
    }





    string string::ltrim() {
        char *temp = new(std::nothrow) char [this->length()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int i = 0;
        while (i < this->length() && this->s.arr[i] == ' ') {
            ++i;
        }

        int k = 0;
        for (int j=i; j<this->length(); ++j) {
            temp[k++] = this->s.arr[j];
        }

        delete[] this->s.arr;

        this->s.array_size = k;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::rtrim() {
        char *temp = new(std::nothrow) char [this->length()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int i = this->length() - 1;
        while (i >= 0 && this->s.arr[i] == ' ') {
            --i;
        }

        int k = 0;
        for (int j=0; j<i+1; ++j) {
            temp[k++] = this->s.arr[j];
        }

        delete[] this->s.arr;

        this->s.array_size = k;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::trim() {
        char *temp = new(std::nothrow) char [this->length()];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        int i = 0;
        int j = this->length() - 1;
        while (i < this->length() && this->s.arr[i] == ' ') {
            ++i;
        }
        while (j >= 0 && this->s.arr[j] == ' ') {
            --j;
        }

        int k = 0;
        for (int p=i; p<j+1; ++p) {
            temp[k++] = this->s.arr[p];
        }

        delete[] this->s.arr;

        this->s.array_size = k;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char [this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; ++i) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    int string::count(const char &letter) const {
        int counts = 0;

        for (int i=0; i<this->length(); i++) {
            if (this->s.arr[i] == letter) {
                counts ++;
            }
        }

        return counts;
    }





    int string::index(const char &letter) const {
        for (int i=0; i<this->length(); i++) {
            if (this->s.arr[i] == letter) {
                return i;
            }
        }

        return -1;
    }





    int string::index(const char *cstring) const {
        const int cstring_length = this->__get_cstring_size(cstring);

        if (cstring_length > this->length() || cstring_length * this->length() == 0) {
            return -1;
        }

        for (int i=0; i<this->length(); i++) {
            if (this->slice(i, i+cstring_length) == cstring) {
                return i;
            }
        }

        return -1;
    }





    int string::index(const std::string &str) const {
        if (this->length() < str.size() || this->length() * str.size() == 0) {
            return -1;
        }

        for (int i=0; i<this->length(); i++) {
            if (this->slice(i, i+str.size()) == str) {
                return i;
            }
        }

        return -1;
    }





    int string::index(const string &str) const {
        return this->s.index(str.s);
    }





    array<int> string::indexes(const char &letter) const {
        array<int> temp;
        for (int i=0; i<this->length(); i++) {
            if (this->s.arr[i] == letter) {
                temp.push_back(i);
            }
        }

        return temp;
    }





    array<int> string::indexes(const char *cstring) const {
        const int cstring_length = this->__get_cstring_size(cstring);
        array<int> temp;

        if (this->length() < cstring_length || this->length() * cstring_length == 0) {
            return temp;
        }

        for (int i=0; i<this->length(); i++) {
            if (this->slice(i, i+cstring_length) == cstring) {
                temp.push_back(i);
            }
        }

        return temp;
    }





    array<int> string::indexes(const std::string &str) const {
        array<int> temp;

        if (this->length() < str.size() || this->length() * str.size() == 0) {
            return temp;
        }

        for (int i=0; i<this->length(); i++) {
            if (this->slice(i, i+str.size()) == str) {
                temp.push_back(i);
            }
        }

        return temp;
    }





    array<int> string::indexes(const string &str) const {
        return this->s.indexes(str.s);
    }





    int string::last_index(const char &letter) const {
        array<int> indexes = this->indexes(letter);

        return (indexes.length() != 0) ? indexes[indexes.length() - 1] : -1;
    }





    int string::last_index(const char *cstring) const {
        array<int> indexes = this->indexes(cstring);

        return (indexes.length() != 0) ? indexes[indexes.length() - 1] : -1;
    }





    int string::last_index(const std::string &str) const {
        array<int> indexes = this->indexes(str);

        return (indexes.length() != 0) ? indexes[indexes.length() - 1] : -1;
    }





    int string::last_index(const string &str) const {
        array<int> indexes = this->indexes(str);

        return (indexes.length() != 0) ? indexes[indexes.length() - 1] : -1;
    }





    array<char> string::split() const {
        return this->s;
    }





    array<string> string::split(const char &letter) const {
        array<string> ret;
        string temp;

        for (int i=0; i<this->length(); ++i) {
            if (this->s.arr[i] == letter) {
                ret.push_back(temp);
                temp.clear();
            }
            else {
                temp.push_back(this->s.arr[i]);
            }
        }
        ret.push_back(temp);

        return ret;
    }





    array<string> string::split(const char *cstring) const {
        array<int> indexes = this->indexes(cstring);
        array<string> ret;

        if (indexes.length() == 0) {
            return ret;
        }
        indexes.push_back(this->length());

        int csize = this->__get_cstring_size(cstring);
        
        string temp = this->slice(0, indexes[0]);
        for (int i=0; i<indexes.length() - 1; ++i) {
            ret.push_back(temp);
            temp = this->slice(indexes[i] + csize, indexes[i+1]);
        }
        ret.push_back(temp);

        return ret;
    }





    array<string> string::split(const std::string &str) const {
        array<int> indexes = this->indexes(str);
        array<string> ret;

        if (indexes.length() == 0) {
            return ret;
        }
        indexes.push_back(this->length());

        string temp = this->slice(0, indexes[0]);
        for (int i=0; i<indexes.length() - 1; ++i) {
            ret.push_back(temp);
            temp = this->slice(indexes[i] + str.length(), indexes[i+1]);
        }
        ret.push_back(temp);

        return ret;
    }





    array<string> string::split(const string &str) const {
        array<int> indexes = this->indexes(str);
        array<string> ret;

        if (indexes.length() == 0) {
            return ret;
        }
        indexes.push_back(this->length());

        string temp = this->slice(0, indexes[0]);
        for (int i=0; i<indexes.length() - 1; ++i) {
            ret.push_back(temp);
            temp = this->slice(indexes[i] + str.length(), indexes[i+1]);
        }
        ret.push_back(temp);

        return ret; 
    }





    array<string> string::partion(const char &letter) const {
        array<string> temp = {"", "", ""};
        
        int first_appearence = -1;
        for (int i=0; i<this->length(); ++i) {
            if (this->s.arr[i] == letter) {
                first_appearence = i;
                break;
            }
        }

        if (first_appearence == -1) {
            temp[0] = *this;
        }
        else {
            temp[0] = this->slice(0, first_appearence);
            temp[1] = letter;
            temp[2] = this->slice(first_appearence+1, this->length());
        }

        return temp;
    }





    array<string> string::partion(const char *cstring) const {
        array<string> temp = {"", "", ""};

        int csize = this->__get_cstring_size(cstring);
        
        int j;
        int first_appearence = -1;
        for (int i=0; i<this->length(); ++i) {
            j = 0;
            while (this->s.arr[i+j] == cstring[j] && j < csize) {
                ++j;
            }
            if (j == csize) {
                first_appearence = i;
                break;
            }
        }

        if (first_appearence == -1) {
            temp[0] = *this;
        }
        else {
            temp[0] = this->slice(0, first_appearence);
            temp[1] = cstring;
            temp[2] = this->slice(first_appearence+csize, this->length());
        }

        return temp;
    }




    array<string> string::partion(const std::string &str) const {
        array<string> temp = {"", "", ""};

        int j;
        int first_appearence = -1;
        for (int i=0; i<this->length(); ++i) {
            j = 0;
            while (this->s.arr[i+j] == str[j] && j < str.length()) {
                ++j;
            }
            if (j == str.length()) {
                first_appearence = i;
                break;
            }
        }

        if (first_appearence == -1) {
            temp[0] = *this;
        }
        else {
            temp[0] = this->slice(0, first_appearence);
            temp[1] = str;
            temp[2] = this->slice(first_appearence+str.length(), this->length());
        }

        return temp;
    }




    array<string> string::partion(const pjf::string &str) const {
        array<string> temp = {"", "", ""};

        int j;
        int first_appearence = -1;
        for (int i=0; i<this->length(); ++i) {
            j = 0;
            while (this->s.arr[i+j] == str[j] && j < str.length()) {
                ++j;
            }
            if (j == str.length()) {
                first_appearence = i;
                break;
            }
        }

        if (first_appearence == -1) {
            temp[0] = *this;
        }
        else {
            temp[0] = this->slice(0, first_appearence);
            temp[1] = str;
            temp[2] = this->slice(first_appearence+str.length(), this->length());
        }

        return temp;
    }





    int string::at(string::iterator &it) const {
        for (int i=0; i<this->length(); i++) {
            if (it == (this->begin() + i)) {
                return i;
            }
        }

        return -1;
    }





    int string::at(string::const_iterator &it) const {
        for (int i=0; i<this->length(); i++) {
            if (it == (this->cbegin() + i)) {
                return i;
            }
        }

        return -1;
    }





    bool string::startswith(const char &letter) const {
        if (this->is_empty()) {
            return false;
        }

        return (this->s.arr[0] == letter);
    }





    bool string::startswith(const char *cstring) const {
        const int cstring_length = this->__get_cstring_size(cstring);

        if (cstring_length <= this->length() && cstring_length > 0) {
            if (this->slice(0, cstring_length) == cstring) {
                return true;
            }
        }
        return false;
    }





    bool string::startswith(const std::string &str) const {
        if (this->length() >= str.size() && str.size() > 0) {
            if (this->slice(0, str.size()) == str) {
                return true;
            }
        }
        return false;
    }





    bool string::startswith(const string &str) const {
        if (this->length() >= str.length() && str.length() > 0) {
            if (this->slice(0, str.length()) == str) {
                return true;
            }
        }
        return false;
    }





    bool string::endswith(const char &letter) const {
        if (this->is_empty()) {
            return false;
        }

        return (this->s.arr[this->length() - 1] == letter);
    }





    bool string::endswith(const char *cstring) const {
        const int cstring_length = this->__get_cstring_size(cstring);

        if (cstring_length <= this->length() && cstring_length > 0) {
            if (this->slice(this->length()-cstring_length, this->length()) == cstring) {
                return true;
            }
        }
        return false;
    }





    bool string::endswith(const std::string &str) const {
        if (this->length() >= str.size() && str.size() > 0) {
            if (this->slice(this->length() - str.size(), this->length()) == str) {
                return true;
            }
        }
        return false;
    }





    bool string::endswith(const string &str) const {
        if (this->length() >= str.length() && str.length() > 0) {
            if (this->slice(this->length() - str.length(), this->length()) == str) {
                return true;
            }
        }
        return false;
    }





    bool string::is_digit() const {
        if (this->is_empty()) {
            return false;
        }

        for (int i=0; i<this->length(); i++) {
            if (!((*this)[i] >= 33 && (*this)[i] <= 64 || (*this)[i] >= 91 && (*this)[i] <= 96 || (*this)[i] >= 123 && (*this)[i] <= 126)) {
                return false;
            }
        }
        return true;
    }





    bool string::is_num() const {
        if (this->is_empty()) {
            return false;
        }

        for (int i=0; i<this->length(); i++) {
            if (!((*this)[i] >= 48 && (*this)[i] <= 57)) {
                return false;
            }
        }
        return true;
    }





    bool string::is_special() const {
        if (this->is_empty()) {
            return false;
        }

        for (int i=0; i<this->length(); i++) {
            if (!((*this)[i] >= 33 && (*this)[i] <= 47 || (*this)[i] >= 58 && (*this)[i] <= 64 || (*this)[i] >= 91 && (*this)[i] <= 96 || (*this)[i] >= 123 && (*this)[i] <= 126)) {
                return false;
            }
        }
        return true;
    }





    bool string::is_alpharithmetic() const {
        if (this->is_empty()) {
            return false;
        }

        for (int i=0; i<this->length(); i++) {
            if (!((*this)[i] >= 65 && (*this)[i] <= 90 || (*this)[i] >= 97 && (*this)[i] <= 122 || (*this)[i] == 32)) {
                return false;
            }
        }
        return true;
    }





    bool string::is_space() const {
        if (this->is_empty()) {
            return false;
        }

        for (int i=0; i<this->length(); i++) {
            if ((*this)[i] != 32) {
                return false;
            }
        }
        return true;
    }





    bool string::is_upper() const {
        string temp = *this;

        return (*this == temp.to_upper());
    }





    bool string::is_lower() const {
        string temp = *this;

        return (*this == temp.to_lower());
    }





    bool string::is_capitalize() const {
        string temp = *this;

        return (*this == temp.capitalize());
    }





    bool string::is_title() const {
        string temp = *this;

        return (*this == temp.title());
    }





    bool string::is_palindrome() const {
        string temp = *this;

        return (*this == temp.rev_string());
    }





    bool string::non_case_comparison(const char *symbol, const char &letter) const {
        string temp = *this;
        char lower_case_letter = letter;
        temp.to_lower();

        if (letter >= 65 && letter <= 90) {
            lower_case_letter = letter + 32;
        }

        if (symbol == ">") {
            return (temp > lower_case_letter);
        }
        else if (symbol == ">=") {
            return (temp >= lower_case_letter);
        }
        else if (symbol == "<") {
            return (temp < lower_case_letter);
        }
        else if (symbol == "<=") {
            return (temp <= lower_case_letter);
        }
        else if (symbol == "==") {
            return (temp == lower_case_letter);
        }
        else if (symbol == "!=") {
            return (temp != lower_case_letter);
        }
        return false;
    }





    bool string::non_case_comparison(const char *symbol, const char *cstring) const {
        string temp1 = *this;
        string temp2 = cstring;
        temp1.to_lower();
        temp2.to_lower();

        if (symbol == ">") {
            return (temp1 > temp2);
        }
        else if (symbol == ">=") {
            return (temp1 >= temp2);
        }
        else if (symbol == "<") {
            return (temp1 < temp2);
        }
        else if (symbol == "<=") {
            return (temp1 <= temp2);
        }
        else if (symbol == "==") {
            return (temp1 == temp2);
        }
        else if (symbol == "!=") {
            return (temp1 != temp2);
        }
        return false;
    }





    bool string::non_case_comparison(const char *symbol, const std::string &str) const {
        string temp1 = *this;
        string temp2 = str;
        temp1.to_lower();
        temp2.to_lower();

        if (symbol == ">") {
            return (temp1 > temp2);
        }
        else if (symbol == ">=") {
            return (temp1 >= temp2);
        }
        else if (symbol == "<") {
            return (temp1 < temp2);
        }
        else if (symbol == "<=") {
            return (temp1 <= temp2);
        }
        else if (symbol == "==") {
            return (temp1 == temp2);
        }
        else if (symbol == "!=") {
            return (temp1 != temp2);
        }
        return false;
    }





    bool string::non_case_comparison(const char *symbol, const string &str) const {
        string temp1 = *this;
        string temp2 = str;
        temp1.to_lower();
        temp2.to_lower();

        if (symbol == ">") {
            return (temp1 > temp2);
        }
        else if (symbol == ">=") {
            return (temp1 >= temp2);
        }
        else if (symbol == "<") {
            return (temp1 < temp2);
        }
        else if (symbol == "<=") {
            return (temp1 <= temp2);
        }
        else if (symbol == "==") {
            return (temp1 == temp2);
        }
        else if (symbol == "!=") {
            return (temp1 != temp2);
        }
        return false;
    }





    char &string::operator[](const int index) {
        if (index > this->length() - 1 || index < 0) {
            std::cout << "Invalid Index Position." << std::endl;
            this->s.~array();
            throw -2;
        }

        return this->s.arr[index];
    }





    string &string::operator=(const char &letter) {
        this->copy(letter);

        return *this;
    }





    string &string::operator=(const char *cstring) {
        this->copy(cstring);

        return *this;
    }





    string &string::operator=(const std::string &str) {
        this->copy(str);

        return *this;
    }





    string &string::operator=(const string &str) {
        if (*this != str) {
            this->copy(str);
        }

        return *this;
    }





    bool string::operator==(const char &letter) const {
        if (this->length() != 1) {
            return false;
        }

        return (this->s.arr[0] == letter);
    }





    bool string::operator==(const char *cstring) const {
        if (this->length() != this->__get_cstring_size(cstring)) {
            return false;
        }

        for (int i=0; i<this->length(); i++) {
            if (this->s.arr[i] != cstring[i]) {
                return false;
            }
        }

        return true;
    }





    bool string::operator==(const std::string &str) const {
        if (this->length() != str.size()) {
            return false;
        }

        for (int i=0; i<this->length(); i++) {
            if (this->s.arr[i] != str[i]) {
                return false;
            }
        }

        return true;
    }





    bool string::operator==(const string &str) const {
        return this->s == str.s;
    }





    bool string::operator<(const char &letter) const {
        return (*this >= letter && this->length() >= 1) ? false : true;
    }





    bool string::operator<(const char *cstring) const {
        return (*this > cstring || *this == cstring) ? false : true;
    }





    bool string::operator<(const std::string &str) const {
        return (*this > str || *this == str) ? false : true;
    }





    bool string::operator<(const string &str) const {
        return (*this > str || *this == str) ? false : true;
    }





    bool string::operator>(const char &letter) const {
        if (this->is_empty()) {
            return false;
        }

        return (this->s.arr[0] > letter);
    }





    bool string::operator>(const char *cstring) const {
        const int min_length = std::min(this->length(), this->__get_cstring_size(cstring));

        for (int i=0; i<min_length; i++) {
            if (this->s.arr[i] > cstring[i]) {
                return true;
            }
            else if (this->s.arr[i] == cstring[i]) {
                continue;
            }
            return false;
        }

        return (this->length() > this->__get_cstring_size(cstring)) ? true : false;
    }





    bool string::operator>(const std::string &str) const {
        const int min_length = std::min(this->length(), (int) str.size());

        for (int i=0; i<min_length; i++) {
            if (this->s.arr[i] > str[i]) {
                return true;
            }
            else if (this->s.arr[i] == str[i]) {
                continue;
            }
            return false;
        }

        return (this->length() > str.size()) ? true : false;
    }





    bool string::operator>(const string &str) const {
        const int min_length = std::min(this->length(), str.length());

        for (int i=0; i<min_length; i++) {
            if (this->s.arr[i] > str[i]) {
                return true;
            }
            else if (this->s.arr[i] == str[i]) {
                continue;
            }
            return false;
        }

        return (this->length() > str.length()) ? true : false;
    }





    bool string::operator>=(const char &letter) const {
        if (this->is_empty()) {
            return false;
        }

        return (this->s.arr[0] >= letter);
    }





    bool string::operator>=(const char *cstring) const {
        const int min_length = std::min(this->length(), this->__get_cstring_size(cstring));

        for (int i=0; i<min_length; i++) {
            if (this->s.arr[i] > cstring[i]) {
                return true;
            }
            else if (this->s.arr[i] == cstring[i]) {
                continue;
            }
            return false;
        }

        return (this->length() >= this->__get_cstring_size(cstring)) ? true : false;
    }





    bool string::operator>=(const std::string &str) const {
        const int min_length = std::min(this->length(), (int) str.size());

        for (int i=0; i<min_length; i++) {
            if (this->s.arr[i] > str[i]) {
                return true;
            }
            else if (this->s.arr[i] == str[i]) {
                continue;
            }
            return false;
        }

        return (this->length() >= str.size()) ? true : false;
    }





    bool string::operator>=(const string &str) const {
        const int min_length = std::min(this->length(), str.length());

        for (int i=0; i<min_length; i++) {
            if (this->s.arr[i] > str[i]) {
                return true;
            }
            else if (this->s.arr[i] == str[i]) {
                continue;
            }
            return false;
        }

        return (this->length() >= str.length()) ? true : false;
    }





    bool string::operator<=(const char &letter) const {
        if (*this == letter) {
            return true;
        }

        return (*this >= letter) ? false : true;
    }





    bool string::operator<=(const char *cstring) const {
        return (*this > cstring) ? false : true;
    }





    bool string::operator<=(const std::string &str) const {
        return (*this > str) ? false : true;
    }





    bool string::operator<=(const string &str) const {
        return (*this > str) ? false : true;
    }





    string string::operator+=(int positions) {
        if (positions < 0) {
            (*this) -= (positions*-1);
        }

        for (int i=0; i<positions; i++) {
            this->push_back('_');
        }

        return *this;
    }





    string string::operator+=(const char &letter) {
        this->push_back(letter);

        return *this;
    }





    string string::operator+=(const char *cstring) {
        this->extend(cstring);

        return *this;
    }





    string string::operator+=(const std::string &str) {
        this->extend(str);

        return *this;
    }





    string string::operator+=(const string &str) {
        this->extend(str);

        return *this;
    }





    string string::operator-=(int positions) {
        if (positions > this->length()) {
            std::cout << "Invalid 'intager' passed." << std::endl;
            this->s.~array();
            throw -2;
        }

        char *temp = new(std::nothrow) char [this->length() - positions];
        if (!temp) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->length() - positions; ++i) {
            temp[i] = this->s.arr[i];
        }
        delete[] this->s.arr;

        this->s.array_size = this->s.array_size - positions;
        this->s.extended_size = this->s.array_size + ARRAY_GAP;

        this->s.arr = new(std::nothrow) char[this->s.extended_size];
        if (!this->s.arr) {BAD_ALLOCATION_MESSAGE; this->s.~array(); throw -1;}

        for (int i=0; i<this->s.array_size; i++) {
            this->s.arr[i] = temp[i];
        }

        delete[] temp;

        return *this;
    }





    string string::operator-=(const char &letter) {
        this->remove(letter, true);

        return *this;
    }





    string string::operator-=(const char *cstring) {
        this->remove(cstring, true);

        return *this;
    }





    string string::operator-=(const std::string &str) {
        this->remove(str, true);

        return *this;
    }





    string string::operator-=(const string &str) {
        this->remove(str, true);

        return *this;
    }





    string string::operator*=(int total_times) {
        int original_length = this->length();

        if (total_times < 0) {
            std::cout << "Only possitive numbers are allowed." << std::endl;
            this->s.~array();
            throw -2;
        }
        else if (total_times == 0) {
            this->clear();
        }
        else {
            for (int i=0; i<total_times-1; i++) {
                this->extend(this->slice(0, original_length));
            }
        }

        return *this;
    }





    string string::operator+(const int positions) const {
        string temp = *this;
        temp += positions;

        return temp;
    }





    string string::operator+(const char &letter) const {
        string temp = *this;
        temp += letter;

        return temp;
    }





    string string::operator+(const char *cstring) const {
        string temp = *this;
        temp += cstring;

        return temp;
    }





    string string::operator+(const std::string &str) const {
        string temp = *this;
        temp += str;

        return temp;
    }





    string string::operator+(const string &str) const {
        string temp = *this;
        temp += str;

        return temp;
    }





    string string::operator-(const int positions) const {
        string temp = *this;
        temp -= positions;

        return temp;
    }





    string string::operator-(const char &letter) const {
        string temp = *this;
        temp -= letter;

        return temp;
    }






    string string::operator-(const char *cstring) const {
        string temp = *this;
        temp -= cstring;

        return temp;
    }





    string string::operator-(const std::string &str) const {
        string temp = *this;
        temp -= str;

        return temp;
    }





    string string::operator-(const string &str) const {
        string temp = *this;
        temp -= str;

        return temp;
    }





    string string::operator*(const int total_times) const {
        string temp = *this;
        temp *= total_times;

        return temp;
    }





    string string::operator++(int) {
        this->push_back('_');

        return *this;
    }





    string string::operator++() {
        this->push_front('_');

        return *this;
    }





    string string::operator--(int) {
        this->pop_back();

        return *this;
    }





    string string::operator--() {
        this->pop_front();

        return *this;
    }





    bool string::__common_iterator::operator==(const string::__common_iterator &_it) const {
        return (this->current == _it.current) ? true : false;
    }





    bool string::__common_iterator::operator!=(const string::__common_iterator &_it) const {
        return (this->current != _it.current) ? true : false;
    }





    bool string::__common_iterator::operator>(const string::__common_iterator &_it) const {
        return (this->current > _it.current) ? true : false;
    }





    bool string::__common_iterator::operator>=(const string::__common_iterator &_it) const {
        return (this->current >= _it.current) ? true : false;
    }





    bool string::__common_iterator::operator<(const string::__common_iterator &_it) const {
        return (this->current < _it.current) ? true : false;
    }





    bool string::__common_iterator::operator<=(const string::__common_iterator &_it) const {
        return (this->current <= _it.current) ? true : false;
    }





    string::__common_iterator &string::__common_iterator::operator++() {
        ++ this->current;

        return *this;
    }





    string::__common_iterator &string::__common_iterator::operator++(int) {
        this->current ++;

        return *this;
    }





    string::__common_iterator &string::__common_iterator::operator--() {
        -- this->current;

        return *this;
    }





    string::__common_iterator &string::__common_iterator::operator--(int) {
        this->current --;

        return *this;
    }





    string::const_iterator::const_iterator() {}





    string::const_iterator::const_iterator(char *elem) {
        this->current = elem;
    }





    const char &string::const_iterator::operator*() const {
        return *this->current;
    }





    const string::const_iterator string::const_iterator::operator+(int value) const {
        string::const_iterator temp = this->current + value;

        return temp;
    }





    const string::const_iterator string::const_iterator::operator-(int value) const {
        string::const_iterator temp = this->current - value;

        return temp;
    }





    string::iterator::iterator() {}





    string::iterator::iterator(char *elem) {
        this->current = elem;
    }





    char &string::iterator::operator*() const {
        return *this->current;
    }





    string::iterator &string::iterator::operator+=(const int value) {
        this->current += value;

        return *this;
    }





    string::iterator &string::iterator::operator-=(const int value) {
        this->current -= value;

        return *this;
    }





    string::iterator string::iterator::operator+(const int value) const {
        string::iterator it = *this;
        it += value;

        return it;
    }





    string::iterator string::iterator::operator-(const int value) const {
        string::iterator it = *this;
        it -= value;

        return it;
    }





    int string::__char_to_int(const char &letter) const {
        switch (letter) {
            case '1':
                return 1;
            case '2':
                return 2;
            case '3':
                return 3;
            case '4':
                return 4;
            case '5':
                return 5;
            case '6':
                return 6;
            case '7':
                return 7;
            case '8':
                return 8;
            case '9':
                return 9;
            default:
                return 0;
        }
    }





    int string::__get_cstring_size(const char *cstring) const {
        int index = 0;
        while (cstring[index] != '\0') {
            ++index;
        }

        return index;
    }





    int string::__get_iter_index(string &str, typename string::iterator &it) const {
        int index = 0;
        for (typename pjf::string::iterator temp_it=str.begin(); temp_it!=(str.end()+1); ++temp_it) {
            if (temp_it == it) {
                break;
            }
            index ++;
        }
        return index;
    }





    int string::__get_iter_index(const string &str, typename string::const_iterator &it) const {
        int index = 0;
        for (typename pjf::string::iterator temp_it=str.begin(); temp_it!=(str.end()+1); ++temp_it) {
            if (temp_it == it) {
                break;
            }
            index ++;
        }
        return index;
    }





    int string::__get_iter_index(std::string &str, typename std::string::iterator &it) const {
        int index = 0;
        for (typename std::string::iterator temp_it=str.begin(); temp_it!=(str.end()+1); ++temp_it) {
            if (temp_it == it) {
                break;
            }
            index ++;
        }
        return index;
    }





    int string::__get_iter_index(const std::string &str, typename std::string::const_iterator &it) const {
        int index = 0;
        for (typename std::string::const_iterator temp_it=str.cbegin(); temp_it!=(str.cend()+1); ++temp_it) {
            if (temp_it == it) {
                break;
            }
            index ++;
        }
        return index;
    }





    bool string::__iter_link_to_string(string &str, string::iterator &it) const {
        for (typename pjf::string::iterator temp_it=str.begin(); temp_it!=str.end(); ++temp_it) {
            if (temp_it == it) {
                return true;
            }
        }
        return false;
    }





    bool string::__iter_link_to_string(const string &str, string::const_iterator &it) const {
        for (typename pjf::string::const_iterator temp_it=str.cbegin(); temp_it!=str.cend(); ++temp_it) {
            if (temp_it == it) {
                return true;
            }
        }
        return false;
    }
}

#endif
