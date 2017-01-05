// 


#ifndef EXCEPTIONS_H
#define EXCEPTIONS_H

#include <string>
#include <stdexcept>


class InputException : public std::exception
{
    public:
        InputException() {}
        virtual ~InputException() {}

        virtual char const * what() const noexcept = 0;
        virtual std::string const & getReason() const = 0;
};


class ArgumentException : public InputException
{
    public:
        ArgumentException(std::string const & reason) :
            reason_ { reason }
        {} 

        char const *        what() const noexcept override { return title_; }
        std::string const & getReason() const override     { return reason_; }

    private:
        char const *      title_ = "\033[1;31merror:\033[0m";
        std::string const reason_;
};

#endif
