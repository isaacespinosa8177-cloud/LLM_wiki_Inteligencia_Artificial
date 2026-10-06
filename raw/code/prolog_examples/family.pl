% family.pl -- the knowledge base used in the Prolog lecture
% (slides "Anatomy of a Prolog Program" and "Querying the Knowledge Base")
%
%   ?- consult('family.pl').        % or just:  ?- [family].

% ---- facts ------------------------------------------------------------
parent(hector, ana).
parent(hector, luis).
parent(ana,    sofia).
parent(luis,   diego).

male(hector).   male(luis).   male(diego).
female(ana).    female(sofia).

% ---- rules ------------------------------------------------------------
father(X, Y) :- parent(X, Y), male(X).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

sibling(X, Y) :-
    parent(P, X), parent(P, Y), X \= Y.

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% ---- starting point for Prolog Lab 01 ---------------------------------
% The assignment asks you to grow this file: more people, more
% generations, a spouse/2 relation, more rules, and a plunit test suite.
% Keep these facts and build on them.

% ---- try these --------------------------------------------------------
%   ?- parent(hector, Who).
%   ?- grandparent(G, sofia).
%   ?- findall(D, ancestor(hector, D), Ds).
%   ?- setof(P, C^parent(P, C), Parents).
%   ?- \+ parent(sofia, _).
